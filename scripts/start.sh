#!/bin/bash

# Navigate to the app directory
cd /home/ubuntu/myapp

# Start the application using Gunicorn
echo "Starting application with Gunicorn..."
sudo gunicorn --bind 0.0.0.0:80 app:app --daemon
