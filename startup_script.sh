#!/bin/sh

set -e
. /app/.venv/bin/activate

exec hypercorn -c hypercorn.toml app.main:api