import datetime

from django.urls import reverse
from django.db import models
from apps.comunes.models import AudtoriaMixin

# Create your models here.
class Persona(AudtoriaMixin):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.CharField("D.N.I.", max_length=12, null=True, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        # ordering = ['apellido', 'nombre']

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)

    def get_absolute_url(self):
        return reverse('persona:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('persona:update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('persona:delete', args=(self.pk,))

    @property
    def edad(self):
        from datetime import date 
        age = date.today().year - self.fecha_nacimiento.year - ((date.today().month, date.today().day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)) 
        return age 
