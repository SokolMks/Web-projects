"""
Django settings for WebProject project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-5*ev5@qoks$n_mvc*82s*j6i1je&6d%h^eb!zd=-w*8t9y1z3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#Heroku host
ALLOWED_HOSTS = ['https://webprogmatching.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'login',
    #'storages', ##This app was installed to use amazon bucket to store media and static files in deployment
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'WebProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WebProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


######
#The uncommented out code is for the amazon mysql server that was used whereas the commented is the original sqlite3 DB
######
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 'default': {
    #      'ENGINE': 'django.db.backends.mysql',
    #      'NAME': 'webprogramming',
    #      'USER': 'root',
    #      'PASSWORD': 'root',
    #  }
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'webprog',
         'USER': 'webproggroup',
         'PASSWORD': 'Admin1234',
         'HOST': 'webprog.cned0hpzkfky.eu-west-2.rds.amazonaws.com',
         'PORT': '3306'
     }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
#########
#Changes were made here to be able to work in deployment on heroku
#Media and static files are hosted on Amazon aws bucket as heroku doesnt keep them
#All of the below comments where lines added in deployment for this
# STATIC_URL = 'https://s3.amazonaws.com:443/%s/static/webprogprofimages/static'
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_STORAGE_BUCKET_NAME = 'webprogprofimages'
# AWS_ACCESS_KEY_ID = 'AKIAJ7GA4RQRQ37RGFAQ'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_QUERYSTRING_AUTH = False
#########
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/loggedIn'
LOGOUT_REDIRECT_URL = '/'

#Settings for the email that is hardcoded to send emails from the server to users that have been liked
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'webprogramminggroupyamm@gmail.com'
EMAIL_HOST_PASSWORD = 'Admin2468'
EMAIL_PORT = 587
