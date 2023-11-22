from project.settings.base import *
import environ
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(".env")

# Sobrescrever as configurações base aqui
SECRET_KEY = env("APP_SECRET_KEY")
ALLOWED_HOSTS = env("APP_ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(" ")
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "../db.sqlite3"),
        "TEST": {
            "NAME": os.path.join(BASE_DIR, "test_database.sqlite3"),
        },
    }
}
