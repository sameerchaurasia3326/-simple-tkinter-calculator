#!/bin/bash
cd /home/ubuntu/myapp
echo "Starting app..."
nohup python3 app.py > app.log 2>&1 &
