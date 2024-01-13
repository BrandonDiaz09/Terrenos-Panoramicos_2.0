#!/bin/bash

# Detiene la ejecución en caso de errores
set -e

# Recopilación de archivos estáticos
echo "Recopilando archivos estáticos..."
# python manage.py collectstatic --no-input

# Realiza migraciones de la base de datos
echo "Realizando migraciones..."
python manage.py makemigrations --no-input
python manage.py migrate

# Imprime el puerto para propósitos de depuración
echo "Port: 8001"

# Inicia Gunicorn en el puerto definido por la variable $PORT
exec gunicorn terrenos_panoramicos.wsgi:application --bind 0.0.0.0:8001