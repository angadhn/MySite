#!/bin/bash

# Check if python3 and pip are available
if command -v python3 &>/dev/null && command -v pip3 &>/dev/null; then
    # Install required Python packages
    pip3 install plotly numpy matplotlib

    # Force run Python preprocessing
    export FORCE_PYTHON=true
fi

# Build the site
bundle exec jekyll build 