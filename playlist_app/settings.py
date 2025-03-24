import os
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
            ],
        },
    },
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

## Simplified static file serving.
## https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Amended this line from staticfiles to static

LOGIN_REDIRECT_URL = '/users/profile/'  # Redirect to the profile page after login
LOGOUT_REDIRECT_URL = '/'  # Redirect to the home page after logout

SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['mixedapes-e0c1f0719094.herokuapp.com',
    '127.0.0.1', 
]

CORS_ALLOWED_ORIGINS = [
    "https://kit.fontawesome.com",
]

# Crispy Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',  # Add crispy_bootstrap4 for forms
    'tape',
    'song',
    'user',
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

ROOT_URLCONF = 'playlist_app.urls'

WSGI_APPLICATION = 'playlist_app.wsgi.application'

## Simplified static file serving.
## https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Amended this line from staticfiles to static

LOGIN_REDIRECT_URL = '/users/profile/'  # Redirect to the profile page after login
LOGOUT_REDIRECT_URL = '/'  # Redirect to the home page after logout

SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['mixedapes-e0c1f0719094.herokuapp.com',
    '127.0.0.1', 
]

CORS_ALLOWED_ORIGINS = [
    "https://kit.fontawesome.com",
]

# Crispy Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',  # Add crispy_bootstrap4 for forms
    'tape',
    'song',
    'user',
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

ROOT_URLCONF = 'playlist_app.urls'

WSGI_APPLICATION = 'playlist_app.wsgi.application'

# Use different database configurations for local and production environments
""" DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

if os.environ.get('DJANGO_ENV') == 'production':
"""
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
"""
else: 
     DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('DB_NAME', 'mixedapes_db'),
    'USER': os.environ.get('DB_USER', 'mixedapes_user'),
    'PASSWORD': os.environ.get('DB_PASSWORD', 'this_password'),
    'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
    'PORT': os.environ.get('DB_PORT', '5432'),
    }
} """
 

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