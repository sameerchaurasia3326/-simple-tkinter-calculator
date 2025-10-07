#!/bin/bash
cd /var/www/html
gunicorn --bind 0.0.0.0:80 app:app > /dev/null 2>&1 &
