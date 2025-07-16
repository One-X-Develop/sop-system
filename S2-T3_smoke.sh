#!/usr/bin/env bash
set -e
echo "=== S2-T3 smoke ==="
cd web-employee
grep -q "axios" package.json
npm run build >/dev/null 2>&1
echo "✓ axios & build ok"
echo "✓ S2-T3 passed"
