#!/bin/bash

# Update the server's package list and install pip for Python 3
sudo apt-get update -y
sudo apt-get install python3-pip -y

# Navigate to the app directory
cd /home/ubuntu/myapp

# Install Python dependencies from requirements.txt
sudo pip3 install -r requirements.txt --break-system-packages
