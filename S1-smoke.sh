#!/usr/bin/env bash
set -e
echo "=== S1 smoke test ==="

docker compose up -d db
sleep 3
docker compose exec -T db psql -U sop -d sop_db -c "TRUNCATE TABLE sops;"

source .venv/bin/activate
PYTHONPATH=. pytest -q

uvicorn app.main:app --port 8001 --log-level warning &
PID=$!
sleep 3

curl -sf http://127.0.0.1:8001/ping >/dev/null
curl -s -X POST http://127.0.0.1:8001/api/sops -H "Content-Type: application/json" \
  -d '{"sop_code":"SMOKE-001","title":"Smoke","description":"test","steps":{"x":1}}' >/dev/null
curl -s http://127.0.0.1:8001/api/sops | grep -q SMOKE-001

kill $PID
echo "✓ all checks passed"
