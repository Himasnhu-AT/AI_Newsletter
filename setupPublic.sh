#!/bin/bash -e

# This script is used to deploy the public release of the project,
# by obfuscating the code and removing unnecessary files to prevent code leakage

# Create a new worktree and checkout a new branch called 'public'
git worktree add public
git checkout --orphan public

# Copy all files to the 'public' branch
cp -r ./* public/

# Configure Git user for the public branch
git config user.name "Deploy from CI"
git config user.email "ci@example.com"  # Add a valid email address

# Install the dependencies
pip3 install -r requirements.txt

# Obfuscate the code using Cython
python3 setup.py build_ext --inplace

# Remove files that are not needed such as Python files and bash files
find public -type f -name "*.py" -delete
find public -type f -name "*.sh" -delete

echo "\"\"\"Entry point for AI Newsletter.\"\"\"

from base import main

if __name__ == \"__main__\":
    main()
" > bot/cython.py

# Commit and push the changes to the public branch
cd public
git add -A
git commit -m 'Deploy Public release'
# Uncomment the following line to push to the remote repository
# git push origin public --force

# Build Docker image
# docker build -f Dockerfile-public -t tos-public:tag .

# Clean up
cd ..
git worktree remove public
