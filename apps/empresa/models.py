from django.db import models
from django.urls import reverse

from apps.comunes.models import Domicilio, CommonStruct, Comunicacion
from apps.persona.models import Persona


class Comercial(CommonStruct):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    domicilios = models.ManyToManyField(Domicilio, related_name='comercial_domicilios', 
                                        blank=True, limit_choices_to = {'active': True})
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='comercial_comunicaciones',
                                            blank=True, limit_choices_to = {'active': True})

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


class Actividad(CommonStruct):
    nombre = models.CharField('Actividad', max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                               null=True, blank=True, verbose_name='Padre')

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.nombre


# class Subactividad(Actividad):
#     actividad = models.OneToOneField(Actividad, on_delete=models.CASCADE, parent_link=True)    


class Empresa(CommonStruct):
    nombre = models.CharField('Nombre de Fantasía', max_length=60)
    razon_social = models.CharField('Razón Social', max_length=60, unique=True)
    cuit = models.CharField('CUIT/CUIL', max_length=13, unique=True, null=True, blank=True)
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE, null=True, blank=True,
                                  limit_choices_to = {'active': True})
    # actividad = models.ForeignKey(Diccionario, on_delete=models.CASCADE, null=True, blank=True, 
    #                               limit_choices_to = {'tabla': 'actividad', 'active': True})
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True, 
                                 limit_choices_to = {'active': True})
    actividades = models.ManyToManyField(Actividad, related_name='empresa_actividades', blank=True, 
                                          limit_choices_to = {'parent__isnull': False, 'active': True})
    domicilios = models.ManyToManyField(Domicilio, related_name='empresa_domicilios',
                                        blank=True, limit_choices_to = {'active': True})
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='empresa_comunicaciones', 
                                            blank=True, limit_choices_to = {'active': True})
    contactos = models.ManyToManyField(Persona, related_name='empresa_contactos', 
                                       blank=True, limit_choices_to = {'active': True})
    observacion = models.TextField(null=True, blank=True)
    referencia_id = models.IntegerField('Referencia Externa', null=True, blank=True, unique=True)
    origen = models.IntegerField(null=True, blank=True)
    planilla = models.IntegerField(null=True, blank=True)

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

    def get_related_url_with_comunication(self):
        return reverse('%s:associate_with_comunication' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_address(self):
        return reverse('%s:associate_with_address' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_contact(self):
        return reverse('%s:associate_with_contact' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_actividad(self):
        return reverse('%s:associate_with_actividad' % self._meta.model_name, args=(self.pk,))
