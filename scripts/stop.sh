#!/bin/bash
echo "Stopping any running Gunicorn processes..."
# The '|| true' part ensures the script doesn't fail if no process is found
sudo pkill gunicorn || true
