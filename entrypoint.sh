#!/bin/bash

# Apply database migrations
python manage.py migrate

# Start Gunicorn server
gunicorn nssf_ewallet.wsgi:application -w 4 -b 0.0.0.0:9000
