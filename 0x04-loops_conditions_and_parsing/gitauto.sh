#!/bin/bash

# Staging changes to commit

git add .

# Ask for the commit message

echo "Enter the commit message:"
read -r commitMessage

# Commit changes

git commit -m "$commitMessage"

# Push Changes

git push
