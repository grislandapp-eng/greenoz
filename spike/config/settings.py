"""Batch 0 spike settings. Synthetic data only; not for production."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Secrets come from the environment; the fallback is for local spike use only.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "spike-only-not-a-secret")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,testserver").split(",")

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "portal",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
    }
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "spike.sqlite3"}}
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Somali ("so") is not a built-in Django language, so it is registered here.
EXTRA_LANG_INFO = {
    "so": {"bidi": False, "code": "so", "name": "Somali", "name_local": "Soomaali"},
}
import django.conf.locale  # noqa: E402

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

LANGUAGE_CODE = "so"
LANGUAGES = [("so", "Soomaali"), ("en", "English"), ("ar", "العربية")]
LOCALE_PATHS = [BASE_DIR / "locale"]
USE_I18N = True
USE_TZ = True
TIME_ZONE = "Africa/Djibouti"
LANGUAGE_COOKIE_NAME = "sl_lang"
LANGUAGE_COOKIE_SAMESITE = "Lax"

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
