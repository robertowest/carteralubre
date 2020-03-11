from django.db import models
from django.urls import reverse

from apps.comunes.models import CommonStruct, Domicilio, Comunicacion, Diccionario
from apps.persona.models import Persona


class Comercial(CommonStruct):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    domicilios = models.ManyToManyField(Domicilio, related_name='comercial_domicilios', blank=True)
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='comercial_comunicaciones', blank=True)

    class Meta:
        verbose_name = 'Comercial'
        verbose_name_plural = 'Comerciales'
        
    def __str__(self):
        if self.persona.apellido is None:
            return "-"
        else:
            return "%s %s" % (self.persona.nombre, self.persona.apellido)

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('comercial:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('comercial:update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comercial:delete', args=(self.pk,))


class Empresa(CommonStruct):
    nombre = models.CharField(max_length=60)
    razon_social = models.CharField('Razón Social', max_length=60, unique=True)
    cuit = models.CharField(max_length=13, unique=True)
    domicilios = models.ManyToManyField(Domicilio, related_name='empresa_domicilios', blank=True)
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='empresa_comunicaciones', blank=True)
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE, null=True, blank=True)
    actividad = models.ForeignKey(Diccionario, on_delete=models.CASCADE, null=True, blank=True)
    referencia_id = models.IntegerField('Referencia Externa', null=True, unique=True)

    # configuración para admin
    list_display = ['razon_social', 'cuit', 'nombre', 'active']
    list_display_links = ['razon_social']
    exclude = []
    search_fields = ['razon_social']
    list_filter = ['comercial']
    date_hierarchy = ''

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razon_social

    def get_absolute_url(self):
        return reverse('empresa:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('empresa:update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('empresa:delete', args=(self.pk,))
