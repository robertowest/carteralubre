import django_heroku
from config.settings_common import *

# ---------------------------------------------------------------------------------------
# CONFIGURACIONES ESPECIFICAS PARA PRODUCCION (HEROKU)
# ---------------------------------------------------------------------------------------


# -------------------------
# ruta de archivos
# -------------------------
FILE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(FILE_DIR)))


# -------------------------
# configuraciones
# -------------------------
DEBUG = False
ALLOWED_HOSTS = ['carteralubre.herokuapp.com']


# -------------------------
# base de datos
# -------------------------
import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


# -------------------------
# heroku
# -------------------------
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
