#!/bin/sh

set -e
. /app/.venv/bin/activate

exec hypercorn -c file:hypercorn.toml app.main:api