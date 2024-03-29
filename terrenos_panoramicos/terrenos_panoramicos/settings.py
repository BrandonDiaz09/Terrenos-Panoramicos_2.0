from decouple import config

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    BASE_DIR / "terrenos_panoramicos" / "credentials.json"
)


SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print(f"Esta en {DEBUG}")
ALLOWED_HOSTS = [
    "*"
]


# Application definition
CSRF_TRUSTED_ORIGINS = [
    'https://terravisiongis.com',
    'https://www.terravisiongis.com',
]

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "storages",
    "rest_framework",
    "rest_framework_gis",
    # Local Apps
    "ventas",
    "users",
    "reuniones",
    "soporte",
    "sig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "terrenos_panoramicos.middelware.ProfileCompletionMiddleware",
]

ROOT_URLCONF = "terrenos_panoramicos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "terrenos_panoramicos.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": config("DATABASE_HOST", default="tvision_dev_db"), 
        "NAME": config("DATABASE_NAME", default="tvision_db"),
        "USER": config("DATABASE_USER", default="tvision_user"),
        "PASSWORD": config("DATABASE_PASSWORD", default="random-contraseña-terra"),
        "PORT": config("DATABASE_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [BASE_DIR / "static",]


STATICFILES_DIRS = [BASE_DIR / "static",]  
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"

# Añade esta línea de código
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"

# En desarrollo, utiliza el almacenamiento local para archivos estáticos y de media
if DEBUG:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

LOGIN_URL = "login"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"