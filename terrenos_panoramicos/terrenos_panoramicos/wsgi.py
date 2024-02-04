"""
WSGI config for terrenos_panoramicos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from decouple import Config, RepositoryEnv

# Asegúrate de que el path al archivo .env es correcto.
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

os.environ['DJANGO_SETTINGS_MODULE'] = Config(RepositoryEnv(dotenv_path)).get('DJANGO_SETTINGS_MODULE', default='terrenos_panoramicos.settings')

application = get_wsgi_application()