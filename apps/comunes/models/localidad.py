from django.db import models
from apps.comunes.models import AudtoriaMixin

from .ciudad import Ciudad


class Localidad(AudtoriaMixin):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    cod_postal = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
