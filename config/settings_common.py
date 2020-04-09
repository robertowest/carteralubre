import os
from config.settings import *

# ---------------------------------------------------------------------------------------
# CONFIGURACIONES ESPECIFICAS PARA DEPURACION
# ---------------------------------------------------------------------------------------


# -------------------------
# aplicaciones del proyecto
# -------------------------
INSTALLED_APPS += [
    'apps.comunes',
    'apps.empresa',
    'apps.persona',
]


# ---------------
# internalización
# ---------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'


# -----------------------------------
# ubicación de los templates públicos
# -----------------------------------
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, "templates"),]


# ------------------
# archivos estáticos
# ------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]


# ----------------
# archivos subidos
# ----------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ------------
# traducciones
# ------------
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]


# --------------------------------------
# agregar contenido a context_processors
# --------------------------------------
# TEMPLATES[0]['OPTIONS']['context_processors'].append('social_django.context_processors.backends')


# ---------------------------------------------
# configucaciones para aplicaciones de terceros
# ---------------------------------------------
# django-crispy-forms
INSTALLED_APPS += ['crispy_forms',]
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# -----------------------------
# redireccionamiento para login
# -----------------------------
LOGIN_URL = '/usuario/login/'
LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/usuario/logout/'
LOGOUT_REDIRECT_URL = '/'


# para que funcione el proceso de registro de usuarios
# esto evitará que se envíe un email e imprimirá el resultado por la consola
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
