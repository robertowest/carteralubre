from django.contrib import admin
from apps.comunes import models


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'cod_postal')
    fields = ('ciudad', 'nombre', 'cod_postal')


admin.site.register(models.Pais)
admin.site.register(models.Ciudad)
admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Domicilio)

admin.site.register(models.Diccionario)