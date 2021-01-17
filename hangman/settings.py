import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "6$Df;f3lE:q#I:A6DkKl5/REX%NNel"
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_extensions',
    "rest_framework",
    'storages',
    'easy_thumbnails',
    "api",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "hangman.urls"
WSGI_APPLICATION = "hangman.wsgi.application"
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "de-ch"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

AWS_STORAGE_BUCKET_NAME = 'hangman-bucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'hangman.storage_backends.MediaStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
WHITENOISE_ROOT = STATIC_ROOT
WHITENOISE_MAX_AGE = 31536000
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [STATIC_ROOT],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

THUMBNAIL_ALIASES = {
    '': {
        'preview': {'size': (800, 600), 'crop': False},
    },
}
THUMBNAIL_DEFAULT_STORAGE = 'hangman.storage_backends.MediaStorage'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

MIN_WORD_LENGTH = 6
MAX_WORD_LENGTH = 15
ACHIEVEMENT_COST = 100
TIMER_INTERVAL = 100


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

django_heroku.settings(locals(), logging=False)

try:
    from .settings_local import *
except:
    pass
