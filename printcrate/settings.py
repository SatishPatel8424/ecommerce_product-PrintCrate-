"""
Django settings for printcrate project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "sdgsdgsdgsdds"

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEPLOY"):
    DEBUG = False
else:
    print("Debug is set to true, this is only suitable for development environments.")
    DEBUG = True

ALLOWED_HOSTS = ["localhost", "*.herokuapp.com",
                 "printcrate.herokuapp.com", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'crispy_forms',
    'django.contrib.staticfiles',
    'printcrate',
    'accounts',
    'cart',
    'checkout',
    'homepage',
    'products',
    'about',
    'contact',
    'storages',
    'sweetify'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'printcrate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents'
            ],
        },
    },
]

WSGI_APPLICATION = 'printcrate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if "DATABASE_URL" in os.environ and os.getenv("DEPLOY"):
    print("Using the PostgreSQL database.")
    DATABASES = {"default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"))}
else:
    print("Falling back to SQLite Database.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# Amazon Web Service Required Settings
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=99999999',
}

AWS_STORAGE_BUCKET_NAME = "django-printcrate-bucket"
AWS_S3_REGION_NAME = "eu-west-2"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

if os.getenv("DEPLOY"):
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    STATIC_URL = "/staticfiles/"
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_LOCATION = "static"
    MEDIAFILES_LOCATION = "media"
    DEFAULT_FILE_LOCATION = "custom_storages.MediaStorage"
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN,
                                     STATICFILES_LOCATION)
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
else:
    STATIC_URL = "/static/"

# Location of files for project operation.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Storage of messages for feedback to user between redirects.
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# URLs to redirect user requiring login & upon login success.
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "profile"

# Defining sweetalert version for sweetify function.
SWEETIFY_SWEETALERT_LIBRARY = "sweetalert2"

# Credentials for functioning contact form page.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST")
EMAIL_HOST_PASSWORD = os.environ.get("HOST_PASS")

# Stripe-required keys.
STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE")
STRIPE_SECRET = os.getenv("STRIPE_SECRET")

# Definition of desired style for forms.
CRISPY_TEMPLATE_PACK = "bootstrap4"
