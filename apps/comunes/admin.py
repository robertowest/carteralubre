from django.contrib import admin

from . import models

admin.site.register(models.Pais)
admin.site.register(models.Ciudad)
admin.site.register(models.Localidad)
admin.site.register(models.Domicilio)
admin.site.register(models.Diccionario)
admin.site.register(models.Comunicacion)


# registra todos los modelos
# se debería ejecutar al final de todo, por si ya existe alguna definición

# from django.apps import apps
# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
