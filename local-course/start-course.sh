#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v pnpm >/dev/null 2>&1 && command -v node >/dev/null 2>&1; then pnpm run build; exec node server.mjs 4173; fi
PNPM_BIN="/Users/jenskristian/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/fallback/pnpm"
NODE_BIN="/Users/jenskristian/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node"
if [ -x "$PNPM_BIN" ] && [ -x "$NODE_BIN" ]; then export PATH="$(dirname "$NODE_BIN"):$PATH"; "$PNPM_BIN" run build; exec "$NODE_BIN" server.mjs 4173; fi
echo "Node.js and pnpm were not found." >&2; exit 1
