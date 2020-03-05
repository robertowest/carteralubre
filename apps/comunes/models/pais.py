from django.db import models
from apps.comunes.models import AudtoriaMixin

class Pais(AudtoriaMixin):
    nombre = models.CharField(max_length=40)
    cod_area_tel = models.CharField('Cód. Area Telef.', max_length=4, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
