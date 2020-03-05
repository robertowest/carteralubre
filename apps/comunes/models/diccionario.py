from django.db import models
from django.urls import reverse

from apps.comunes.models import AudtoriaMixin


TABLA = (('actividad', 'Actividades'), ('domicilio', 'Domicilios'),)


class Diccionario(AudtoriaMixin):
    texto = models.CharField(max_length=150)
    tabla = models.CharField(max_length=45, choices=TABLA, default='actividad')

    def __str__(self):
        return "%s (%s)" % (self.texto, self.get_tabla_display())

    def get_texto(self):
        return str(self.texto).capitalize()

    def get_absolute_url(self):
        return reverse('comunes:dicc_info', args=(self.pk,))

    def get_update_url(self):
        return reverse('comunes:dicc_modif', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comunes:dicc_borrar', args=(self.pk,))

    class Meta:
        verbose_name = 'Diccionario'
        verbose_name_plural = 'Diccionarios'