"""
Django settings for drzwikumi project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-z2*vu0%r=vd^x4gfcd-&848dm$gm^i+0020@-ov^au!qbq-6x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['139.162.163.67']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drzwikumiApp.apps.DrzwikumiappConfig',
    'bootstrap4',
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

ROOT_URLCONF = 'drzwikumi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
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

WSGI_APPLICATION = 'drzwikumi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
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

STATICFILES_DIRS = (
    BASE_DIR + '/templates/css/',
    BASE_DIR + '/templates/js/',
    BASE_DIR + '/templates/contactform/',
    BASE_DIR + '/templates/lib/bootstrap/css/',
    BASE_DIR + '/templates/lib/bootstrap/js/',
    BASE_DIR + '/templates/lib/owlcarousel/',
    BASE_DIR + '/templates/lib/venobox/',
    BASE_DIR + '/templates/img/',
    BASE_DIR + '/templates/img/slider/',
    BASE_DIR + '/templates/img/venubox/',
    BASE_DIR + '/templates/lib/appear/',
    BASE_DIR + '/templates/lib/animate/',
    BASE_DIR + '/templates/lib/appear/',
    BASE_DIR + '/templates/lib/bootstrap/js/',
    BASE_DIR + '/templates/lib/bootstrap/css/',
    BASE_DIR + '/templates/lib/bootstrap/fonts/',
    BASE_DIR + '/templates/lib/easing/',
    BASE_DIR + '/templates/lib/font-awesome/css/',
    BASE_DIR + '/templates/lib/font-awesome/fonts/',
    BASE_DIR + '/templates/lib/isotope/',
    BASE_DIR + '/templates/lib/jquery/',
    BASE_DIR + '/templates/lib/knob/',
    BASE_DIR + '/templates/lib/nivo-slider/css/',
    BASE_DIR + '/templates/lib/nivo-slider/js/',
    BASE_DIR + '/templates/lib/nivo-slider/img/',
    BASE_DIR + '/templates/lib/owlcarousel/',
    BASE_DIR + '/templates/lib/parallax/',
    BASE_DIR + '/templates/lib/venobox/',
    BASE_DIR + '/templates/lib/wow/',
)

DOOR_IMAGES = BASE_DIR + '/templates/img/offer'

staticfiles_list = list(STATICFILES_DIRS)
for directory in os.listdir(DOOR_IMAGES):
    for subdirectory in os.listdir('{}/{}/'.format(DOOR_IMAGES, directory)):
        staticfiles_list.append('{}/{}/{}/'.format(DOOR_IMAGES, directory, subdirectory))
        if directory == 'roomdoors':
            for serie in os.listdir('{}/{}/{}/'.format(DOOR_IMAGES, directory, subdirectory)):
                if os.path.isdir('{}/{}/{}/{}/'.format(DOOR_IMAGES, directory, subdirectory, serie)):
                    staticfiles_list.append('{}/{}/{}/{}/'.format(DOOR_IMAGES, directory, subdirectory, serie))

STATICFILES_DIRS = tuple(staticfiles_list)

STATIC_ROOT = 'static'
STATIC_URL = '/templates/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.wp.pl'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'powiadomienia.kumi@wp.pl'
EMAIL_HOST_PASSWORD = 'adikurwakodi12'
