#!/bin/bash -e

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Build extensions
python3 setup.py build_ext --inplace

# Start Docker Compose in detached mode
docker compose up -d 

# # Clean up build artifacts and virtual environment
# rm -rf venv/
rm -rf build/
rm -rf ./Bot/**/*.so
rm -rf ./Bot/**/*.c
