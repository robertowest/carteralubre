from django.db import models
from django.urls import reverse

from apps.comunes.models import AudtoriaMixin

TIPO = (('tel', 'Teléfono'), ('movil', 'Celular'), ('wa', 'WhatsApp'),
        ('email', 'Correo Electrónico'), ('face', 'Facebook'),
        ('twitt', 'Twitter'), ('link', 'LinkedIn'))


class Comunicacion(AudtoriaMixin):
    tipo = models.CharField(max_length=5, choices=TIPO, default='movil')
    texto = models.CharField(max_length=150)

    def __str__(self):
        return "%s: %s" % (self.get_tipo_display(), self.texto)

    def get_absolute_url(self):
        return reverse('comunes:comu_info', args=(self.pk,))

    def get_update_url(self):
        return reverse('comunes:comu_modif', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comunes:comu_borrar', args=(self.pk,))

    class Meta:
        verbose_name = 'Comunicacion'
        verbose_name_plural = 'Comunicaciones'
