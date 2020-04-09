import os
from config.settings_common import *

# ---------------------------------------------------------------------------------------
# CONFIGURACIONES ESPECIFICAS PARA DEPURACION
# ---------------------------------------------------------------------------------------


# ---------------
# host permitidos
# ---------------
ALLOWED_HOSTS = ['*']


# -------------
# base de datos
# -------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'clientes_dev',
#         'USER': 'roberto',
#         'PASSWORD': 'roberto',
#         'HOST': '192.168.1.2',
#         'PORT': '3306',
#     }
# }


# --------------------------------
# configuración para la contraseña
# --------------------------------
AUTH_PASSWORD_VALIDATORS = []


# --------------------------------------
# agregar contenido a context_processors
# --------------------------------------
# TEMPLATES[0]['OPTIONS']['context_processors'].append('social_django.context_processors.backends')


# ------------------------------------------------------
# aplicaciones de terceros, middleware y configuraciones
# solo para entorno de desarrollo
# ------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug
]

# debug 
INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1', '172.20.0.1']  # (gateway del docker)
