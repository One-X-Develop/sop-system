#!/usr/bin/env bash
set -e
echo "=== S2-T1 smoke ==="
cd web-employee
npm run build >/dev/null 2>&1
echo "✓ Vite build ok"
echo "✓ S2-T1 passed"
