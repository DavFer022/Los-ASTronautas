#!/bin/bash
# Script de ejecución del experimento en entornos Unix / Bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$( dirname "$SCRIPT_DIR" )"
python3 "$SCRIPT_DIR/run_experiment.py"
