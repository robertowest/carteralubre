import datetime

from django.urls import reverse
from django.db import models

from apps.comunes.models import CommonStruct, Comunicacion, Domicilio
from apps.comunes.functions import get_app_name, get_model_name


class Persona(CommonStruct):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.CharField('DNI', max_length=12, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', blank=True, null=True)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, null=True, blank=True,
                                  limit_choices_to = {'active': True})
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='persona_comunicaciones', 
                                            blank=True, limit_choices_to = {'active': True})

    # configuración para admin
    list_display = ['apellido', 'nombre', 'documento', 'active']
    search_fields = ['nombre', 'apellido']
    list_filter = ['ciudad', 'localidad']

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)

    @property
    def edad(self):
        if self.fecha_nacimiento is None:
            return None            
        else:
            from datetime import date
            age = date.today().year - self.fecha_nacimiento.year - ((date.today().month, date.today().day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)) 
            return age

    @property
    def nombre_completo(self):
        return "%s %s" % (self.nombre, self.apellido)

    def get_related_url_with_address(self):
        return reverse('%s:associate_with_address' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_contact(self):
        return reverse('%s:associate_with_contact' % self._meta.model_name, args=(self.pk,))
