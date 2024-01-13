from decouple import config
from pathlib import Path
from google.oauth2 import service_account

# Define the base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Configure Google Service Account Credentials For Bucket Data
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    BASE_DIR / "terrenos_panoramicos" / "credentials.json"
)

# Set your Django Secret Key from environment variables
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

# Define allowed hostnames for your application
ALLOWED_HOSTS = [
    "terravision-c7yvkfhtla-uc.a.run.app",
    "terravisiongis.com",
    "*",
    "34.31.38.196",
    "10.128.0.2",
]

# Configure trusted origins for CSRF protection
CSRF_TRUSTED_ORIGINS = ["http://34.31.38.196"]

# List of installed Django applications
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

# Define middleware settings
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

# Define the root URL configuration
ROOT_URLCONF = "terrenos_panoramicos.urls"

# Configure template settings
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

# Define the WSGI application
WSGI_APPLICATION = "terrenos_panoramicos.wsgi.application"

# Configure the database settings
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "tvision_dev_db",
        "NAME": "tvision_db",
        "USER": "tvision_user",
        "PASSWORD": "2014Mel&MeTVProd",
        "PORT": "5432",
    }
}

# Define password validation settings
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

# Set the default language code
LANGUAGE_CODE = "es"

# Set the default time zone
TIME_ZONE = "UTC"

# Enable internationalization
USE_I18N = True

# Enable localization
USE_L10N = True

# Enable timezone support
USE_TZ = True

# Import other configurations...

# Configure Google Cloud Storage settings
GS_BUCKET_NAME = "django-qa"
GS_LOCATION = "us-south1"
STATIC_URL = "https://storage.googleapis.com/{}/static/".format(GS_BUCKET_NAME)
MEDIA_URL = "https://storage.googleapis.com/{}/media/".format(GS_BUCKET_NAME)

# Specify the static root directory
STATIC_ROOT = BASE_DIR / "staticfiles"

# Define additional static file directories
STATICFILES_DIRS = (BASE_DIR / "static",)

# Specify static file finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Define the login URL
LOGIN_URL = "login"

# Set the default auto field for Django models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configure the default file storage for media files
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"

# Configure the default file storage for static files
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
