#!/bin/bash
set -e

if [ "$ENVIRONMENT" = "production" ]; then
    echo "Recopilando archivos estáticos..."
    python manage.py collectstatic --no-input

    echo "Realizando migraciones..."
    python manage.py migrate

    echo "Iniciando Gunicorn..."
    exec gunicorn terrenos_panoramicos.wsgi:application --bind 0.0.0.0:8001
else
    echo "Iniciando servidor de desarrollo..."
    python manage.py runserver 0.0.0.0:8001
fi
