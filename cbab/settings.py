"""
Django settings for CBAB project.
"""

import os
from pathlib import Path


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

BASE_DIR = Path(__file__).resolve().parent.parent

REDMINE_ID = os.environ.get("REDMINE_ID", "7601")
ACDH_IMPRINT_URL = "https://imprint.acdh.oeaw.ac.at/"
SECRET_KEY = os.environ.get("SECRET_KEY", "rlYWFQbFuwofjjafjwo")


if os.environ.get("DEBUG", False):
    DEBUG = True
else:
    DEBUG = False

ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]

# Application definition

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap3",
    "django_extensions",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "webpage",
    "vocabs",
    "places",
    "burials",
    "bib",
    "browsing",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"
CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    )
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SPAGHETTI_SAUCE = {
    "apps": ["vocabs", "places", "burials", "bib"],
    "show_fields": False,
    "exclude": {"auth": ["user"]},
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cbab.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "cbab.wsgi.application"

if os.environ.get("POSTGRES_DB"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "cbab"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTEGRES_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "CET"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# To do: if Z_BASE_URL, Z_COLLECTION are missing get_zotero_url() throws an error, this
# workaround (setting empty ones) prevents the errors but still produces invalid urls - please fix
Z_BASE_URL = "https://www.zotero.org/mgavranovic/items/collectionKey"
Z_COLLECTION = "4CRPGG6W"
