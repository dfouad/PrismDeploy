"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p2!o8bh6uv--#4!@hkt-6#+1om0-__piyhf-968il9sr*&mkec'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AdminPanel',
    'Students',
    'common_App',
    #'django_extensions',
    'multiselectfield',
    'import_export',
    'phonenumber_field',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')],
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

WSGI_APPLICATION = 'Project.wsgi.application'
  

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
        'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'neondb', 
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_cPWrd0MoF9gt',
        'HOST': 'ep-winter-waterfall-abzb5op5-pooler.eu-west-2.aws.neon.tech', 
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': str(BASE_DIR / 'db.sqlite3'), 
    # }
}
# 'NAME': BASE_DIR / 'db.sqlite3',

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/




#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_origin')]
#STATIC_ROOT = os.path.join(BASE_DIR , 'static')

# Collects static files here
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add this for serving in production
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

#STATICFILES_DIRS = [os.path.join(BASE_DIR , 'Project/static')]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


#ALLOWED_HOSTS = ['192.168.1.50']
#ALLOWED_HOSTS = ["dfouad.pythonanywhere.com","127.0.0.1","localhost:8000","prismdeploy-production.up.railway.app"]
ALLOWED_HOSTS = ['https://www.prism-edu.com','www.prism-edu.com','127.0.0.1','localhost:8000','prismdeploy-production.up.railway.app','wwweb-production.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://www.prism-edu.com','https://prismdeploy-production.up.railway.app']


