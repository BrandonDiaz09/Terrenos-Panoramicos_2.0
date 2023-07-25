"""
WSGI config for terrenos_panoramicos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

from decouple import config, AutoConfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terrenos_panoramicos.settings')
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
AutoConfig(search_path=dotenv_path)

application = get_wsgi_application()