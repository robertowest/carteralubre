from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    model = models.Empresa
    list_display = model.list_display
    list_display_links = model.list_display_links
    # exclude = model.exclude
    search_fields = model.search_fields
    # list_filter = model.list_filter
    # date_hierarchy = model.date_hierarchy