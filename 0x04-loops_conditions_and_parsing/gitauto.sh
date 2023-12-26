#!/bin/bash

# Staging changes to commit

git add .

# Ask for the commit message

echo "Enter the commit message: \n"
read commitMessage

# Commit changes

git commit -m "$commitMessage"

# Push Changes

git push
