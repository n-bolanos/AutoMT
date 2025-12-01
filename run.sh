#!/bin/bash

# Activate virtual environment and run the main script

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if .venv exists
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo "Error: .venv folder not found in $SCRIPT_DIR"
    echo "Please create a virtual environment first with: python -m venv .venv"
    exit 1
fi

# Activate the virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment"
    exit 1
fi

# Run the main script
python "$SCRIPT_DIR/main.py"

# Store the exit code
EXIT_CODE=$?

# Deactivate the virtual environment
deactivate

exit $EXIT_CODE
