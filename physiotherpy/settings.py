
import datetime
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'ynewfe51@!^zmn@$a_%ebpkmpg=cg_&ll0-xmud+p0k5fq_l%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['127.0.0.1','physioapiproject.herokuapp.com']
ALLOWED_HOSTS = ['192.168.1.106']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'Accounts',
    'Clinic',
    'Physiotherapist',
    'MyAdmin',
    'Patient',
    'Game',
    'ExeercisePlan',
    'Session',
    'Favourite',
    'Observation',
    'Scores'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'physiotherpy.urls'

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

WSGI_APPLICATION = 'physiotherpy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TheFinalPhysioDB',
        'USER': 'postgres',
        'PASSWORD': '42105518',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djth96gse98hl',
        'USER': 'bttliepuqbmkhr',
        'PASSWORD': '30c12def79107ea8adccd6ae64824cbc8aa72d95ccb01bf9895134b1b1b6aa31',
        'HOST': 'ec2-54-158-232-223.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}




REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],


    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


AUTH_USER_MODEL = 'Accounts.NewUser'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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






LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True






