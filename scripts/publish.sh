#!/usr/bin/env bash
# Publish dist/ to an S3-compatible bucket (the site behind https://brand.flovatar.com).
# Usage: scripts/publish.sh [--dry-run]      (run `python3 tools/build.py` first)
# Config: environment variables, or a gitignored scripts/publish.local.env that sets them:
#   BUCKET        target bucket name (required)
#   S3_ENDPOINT   S3 API endpoint URL (required for non-AWS storage such as Cloudflare R2)
#   AWS_PROFILE   aws CLI profile with write access to the bucket (optional)
# Each file type is uploaded with an explicit Content-Type and Cache-Control; a final pass deletes removed files.
set -euo pipefail
cd "$(dirname "$0")/.."
[[ -f scripts/publish.local.env ]] && source scripts/publish.local.env
: "${BUCKET:?set BUCKET (or create scripts/publish.local.env)}"
DRY=()
[[ "${1:-}" == "--dry-run" ]] && DRY=(--dryrun)
[[ -f dist/index.html ]] || { echo "dist/ missing: run python3 tools/build.py" >&2; exit 1; }
if ls dist/fonts/*.woff2 >/dev/null 2>&1; then :; else echo "WARNING: dist/fonts empty (dist-private/fonts missing?)" >&2; fi

S3=(aws)
[[ -n "${AWS_PROFILE:-}" ]] && S3+=(--profile "$AWS_PROFILE")
[[ -n "${S3_ENDPOINT:-}" ]] && S3+=(--endpoint-url "$S3_ENDPOINT")
S3+=(s3)
SHORT="public, max-age=300"
DAY="public, max-age=86400"
IMMUTABLE="public, max-age=31536000, immutable"

# sync_type <cache-control> <content-type> <include patterns...>
sync_type() {
  local cc="$1" ct="$2"; shift 2
  local inc=()
  for p in "$@"; do inc+=(--include "$p"); done
  "${S3[@]}" sync dist/ "s3://$BUCKET/" ${DRY[@]+"${DRY[@]}"} --only-show-errors --exclude "*" "${inc[@]}" \
    --content-type "$ct" --cache-control "$cc"
}

# content-hashed CSS/JS/fonts under static/ → 1 year immutable
"${S3[@]}" sync dist/static/ "s3://$BUCKET/static/" ${DRY[@]+"${DRY[@]}"} --only-show-errors --exclude "*" --include "*.css" \
  --content-type "text/css; charset=utf-8" --cache-control "$IMMUTABLE"
"${S3[@]}" sync dist/static/ "s3://$BUCKET/static/" ${DRY[@]+"${DRY[@]}"} --only-show-errors --exclude "*" --include "*.js" \
  --content-type "text/javascript; charset=utf-8" --cache-control "$IMMUTABLE"
"${S3[@]}" sync dist/static/ "s3://$BUCKET/static/" ${DRY[@]+"${DRY[@]}"} --only-show-errors --exclude "*" --include "*.woff2" \
  --content-type "font/woff2" --cache-control "$IMMUTABLE"

# documents → 5 minutes
sync_type "$SHORT" "text/html; charset=utf-8" "*.html"
sync_type "$SHORT" "text/plain; charset=utf-8" "*.md" "*.txt"
sync_type "$SHORT" "application/json; charset=utf-8" "*.json"
sync_type "$SHORT" "application/xml; charset=utf-8" "*.xml"
sync_type "$SHORT" "text/css; charset=utf-8" "tokens/*.css"

# media (stable names) → 1 day
sync_type "$DAY" "image/svg+xml" "*.svg"
sync_type "$DAY" "image/png" "*.png"
sync_type "$DAY" "image/jpeg" "*.jpg" "*.jpeg"
sync_type "$DAY" "image/webp" "*.webp"
sync_type "$DAY" "image/gif" "*.gif"
sync_type "$DAY" "application/pdf" "*.pdf"
sync_type "$DAY" "font/woff2" "fonts/*.woff2"

# final pass: delete objects that no longer exist locally (already-uploaded files are skipped)
"${S3[@]}" sync dist/ "s3://$BUCKET/" ${DRY[@]+"${DRY[@]}"} --only-show-errors --delete --exclude "static/*" --exclude "_share/*"   # _share/ = temporary shares, never deleted by publish
"${S3[@]}" sync dist/static/ "s3://$BUCKET/static/" ${DRY[@]+"${DRY[@]}"} --only-show-errors --delete
echo "published dist/ → s3://$BUCKET/"
