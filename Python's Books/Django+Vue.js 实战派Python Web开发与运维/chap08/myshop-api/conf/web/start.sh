#!/bin/bash
python manage.py makemigrations&&
python manage.py migrate&&
gunicorn -c gunicorn.py myshop.wsgi:application