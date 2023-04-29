from pathlib import Path
import os

from django.urls import reverse_lazy
from .logging_formatters import CustomJsonFormatter


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v$n2$x(_t@7*+t^=#b*41_k_cik01$120dppi)-@-6_xfquhs+'

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
    
    'crispy_forms',
    'crispy_bootstrap5',
    'debug_toolbar',
    'rest_framework',
    # 'django_celery_results',
    
    'films.apps.FilmsConfig',
    'users.apps.UsersConfig',
]

CRISPY_ALLOWED_TEMPLATES_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fiiilm', 
        'USER': 'matvey',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
        # 'PORT': '6432',

    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = '/login'


################## CELERY ##################

REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZEAR ='json'

################## LOGGING ##################

# any types of formatters you can fin on oficcial logging page... +_+ 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
        'main_format': {
            # logging message formatter
            'format': "[{levelname} - {asctime} - {module} - {message}]",
            'style': "{",
        },
        
        'json_format': {
            # () - значит что мы принимаем class 
            '()': CustomJsonFormatter,
        }
    },
    
    # обработчик логов
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'main_format',
        },
        
        # logging for django
        'django_file': {
            'class': 'logging.FileHandler',
            'formatter': 'json_format',
            'filename': 'django_info.log'
        },
        
        # logging for celery
        'celery_file': {
            'class': 'logging.FileHandler',
            'formatter': 'json_format',
            'filename': 'celery_info.log'            
        }
    },
    
    # объект для логгирования сообщений
    'loggers': {
        'django': {
            'handlers': ['django_file', 'console'],
            'level': 'INFO',  
            'propagate': True,          
        }, 
        
        'celery': {
            'handlers': ['celery_file', 'console'],
            'level': 'INFO',  
            'propagate': True,          
        }, 
    },
    
}

