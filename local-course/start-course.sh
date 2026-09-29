#!/bin/sh
set -eu
cd "$(dirname "$0")"
if ! command -v node >/dev/null 2>&1 || ! command -v pnpm >/dev/null 2>&1; then
  echo "Install Node.js and pnpm, then run pnpm install --frozen-lockfile in local-course/." >&2
  exit 1
fi
if [ ! -d node_modules ]; then
  echo "Dependencies are missing. Run pnpm install --frozen-lockfile in local-course/." >&2
  exit 1
fi
pnpm run build
exec node server.mjs 4173
