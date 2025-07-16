#!/usr/bin/env bash
set -e
echo "=== S2-T2 smoke ==="
cd web-employee
grep -q "react-router-dom" package.json
npm run build >/dev/null 2>&1
echo "✓ router & build ok"
echo "✓ S2-T2 passed"
