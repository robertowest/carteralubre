from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Persona)
class PersonaAdmin(admin.ModelAdmin):
    model = models.Persona
    list_display = model.list_display
    list_display_links = model.list_display_links
    search_fields = model.search_fields
