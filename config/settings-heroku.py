import django_heroku
from config.settings import *

# ---------------------------------------------------------------------------------------
# CONFIGURACIONES ESPECIFICAS PARA PRODUCCION (HEROKU)
# ---------------------------------------------------------------------------------------

# ruta del proyecto: os.path.join(BASE_DIR, ...)
FILE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(FILE_DIR)))
DEBUG = False
ALLOWED_HOSTS = ['carteralubre.herokuapp.com']


# -------------------------
# aplicaciones del proyecto
# -------------------------
INSTALLED_APPS += [
    'apps.comunes',
    'apps.empresa',
    'apps.persona',
]


# base de datos
import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


# internalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'


# archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# archivos subidos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# heroku
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# # python manage.py collectstatic
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# Activate Django-Heroku.
# django_heroku.settings(locals())
