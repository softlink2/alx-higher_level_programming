#!/bin/bash
echo "please input your commit message"
read=MESSAGE
git add .
git commit -m $"MESSAGE"
git push
