#!/bin/sh

python manage.py collectstatic --no-input
python manage.py makemigrations --no-input
python manage.py migrate

echo "Port: $PORT"

# Start Gunicorn on the port defined by $PORT
exec gunicorn terrenos_panoramicos.wsgi:application --bind 0.0.0.0:$PORT