# ---------------------------------------------------------------------------------------
# CONFIGURACIONES ESPECIFICAS PARA PRODUCCION
# ---------------------------------------------------------------------------------------
import os
import dj_database_url

from config.settings.base import *
from decouple import config


# -------------------------
# ruta de archivos
# -------------------------
# FILE_DIR = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(FILE_DIR)))


# -------------------------
# configuraciones
# -------------------------
ALLOWED_HOSTS = ['carteralubre.herokuapp.com']


# -------------------------
# base de datos
# -------------------------
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


# -------------------------------------------------------------------
# archivos en el servidor
# -------------------------------------------------------------------
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# -------------------------
# heroku
# -------------------------
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
