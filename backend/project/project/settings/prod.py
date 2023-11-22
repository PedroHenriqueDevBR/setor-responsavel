from project.settings.base import *
import os

# Sobrescrever as configurações base aqui
SECRET_KEY = os.environ.get("APP_SECRET_KEY")
ALLOWED_HOSTS = str(os.environ.get("APP_ALLOWED_HOSTS") or "*").split(" ")
CSRF_TRUSTED_ORIGINS = str(os.environ.get("CSRF_TRUSTED_ORIGINS") or "*").split(" ")
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": int(os.environ.get("POSTGRES_PORT")),
    }
}
