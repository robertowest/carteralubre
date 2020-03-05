from django.db import models
from django.urls import reverse

from apps.comunes.models import AudtoriaMixin

from apps.comunes.models.pais import Pais
from apps.comunes.models.ciudad import Ciudad
from apps.comunes.models.localidad import Localidad

TIPO = (('Av.', 'Avenida'), ('Calle', 'Calle'), ('Pje.', 'Pasaje'))

class Domicilio(AudtoriaMixin):
    tipo = models.CharField(max_length=5, choices=TIPO, default='Calle')
    calle = models.CharField(max_length=40)
    numero = models.IntegerField('Número', null=True, blank=True)
    piso = models.CharField(max_length=2, null=True, blank=True)
    puerta = models.CharField(max_length=2, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.calle, self.numero)

    def get_absolute_url(self):
        # reverse('comunes:domi_info', kwargs={'pk': self.pk})
        return reverse('comunes:domi_info', args=(self.pk,))

    def get_update_url(self):
        return reverse('comunes:domi_modif', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comunes:domi_borrar', args=(self.pk,))

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'