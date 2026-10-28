#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_design_atlas info
PYTHONPATH=src python -m gbt_design_atlas check --payload '{}'
PYTHONPATH=src python -m gbt_design_atlas run   --payload '{}'
