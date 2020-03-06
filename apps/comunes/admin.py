from django.contrib import admin
from apps.comunes import models


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'cod_postal')
    fields = ('ciudad', 'nombre', 'cod_postal')


admin.site.register(models.Pais)
admin.site.register(models.Ciudad)
admin.site.register(models.Localidad, LocalidadAdmin)


@admin.register(models.Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    model = models.Domicilio
    list_display = model.list_display
    list_display_links = model.list_display_links
    # exclude = model.exclude
    search_fields = model.search_fields
    list_filter = model.list_filter
    # date_hierarchy = model.date_hierarchy
    list_per_page = 25


@admin.register(models.Comunicacion)
class ComunicacionAdmin(admin.ModelAdmin):
    model = models.Comunicacion
    list_display = model.list_display
    list_display_links = model.list_display_links
    list_per_page = 25


admin.site.register(models.Diccionario)
