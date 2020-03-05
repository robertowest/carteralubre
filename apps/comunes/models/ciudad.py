from django.db import models
from apps.comunes.models import AudtoriaMixin

from .pais import Pais

class Ciudad(AudtoriaMixin):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)  # , null=True, blank=True
    nombre = models.CharField(max_length=40)
    cod_area_tel = models.CharField('Cód. Area Telef.', max_length=4, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
