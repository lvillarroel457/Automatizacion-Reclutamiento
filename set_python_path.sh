#!/bin/bash

# Get the absolute path of the current directory
current_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Export the current directory path to PYTHONPATH
export PYTHONPATH="$current_dir"
