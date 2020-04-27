# ---------------------------------------------------------------------------------------
# CONFIGURACIONES ESPECIFICAS PARA DESARROLLO
# ---------------------------------------------------------------------------------------
from config.settings.base import *


# -------------------------------------------------------------------
# host permitidos
# -------------------------------------------------------------------
ALLOWED_HOSTS = ['*']


# -------------------------
# base de datos
# -------------------------
DATABASES = {
    # # casa
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'carteralubre',
    #     'USER': 'root',
    #     'PASSWORD': 'roberto',
    #     'HOST': '172.17.0.2',
    #     'PORT': '3306',
    # },

    # lubre
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carteralubre',
        'USER': 'roberto',
        'PASSWORD': 'roberto',
        'HOST': '192.168.1.2',
        'PORT': '3306',
    },
}


# -------------------------------------------------------------------
# configuración para la contraseña
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = []


# -------------------------------------------------------------------
# aplicaciones de terceros, middleware y configuraciones
# solo para entorno de desarrollo
# -------------------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug
]

INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1', '172.20.0.1']  # (gateway del docker)
