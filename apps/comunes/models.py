from django.db import models
from django.urls import reverse
from datetime import datetime


class CommonStruct(models.Model):
    active = models.BooleanField('Activo', default=True)
    created = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True, blank=True)
    created_by = models.CharField('Creado por', max_length=15, editable=False, null=True, blank=True)
    modified = models.DateTimeField('Modificado', auto_now_add=True, editable=False, null=True, blank=True)
    modified_by = models.CharField('Modif. por', max_length=15, editable=False, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        super(CommonStruct, self).save(*args, **kwargs)

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self):
        super(CommonStruct, self).delete()

    def get_fields(self):
        """Devuelve una lista con los nombres de todos los campos"""
        fields = []
        for f in self._meta.fields:
            # comprobamos que el campo sea del tipo que queremos visualizar
            if f.editable and f.name not in ('id', 'active'):
                try:
                    value = getattr(self, f.name)
                    if value:
                        fields.append({'name':f.verbose_name, 'value':value,})
                except:
                    value = None
        return fields


class Pais(CommonStruct):
    nombre = models.CharField(max_length=40)
    cod_area_tel = models.CharField('Cód. Area Telef.', max_length=4, null=True, blank=True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre


class Ciudad(CommonStruct):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)  # , null=True, blank=True
    nombre = models.CharField(max_length=40)
    cod_area_tel = models.CharField('Cód. Area Telef.', max_length=4, null=True, blank=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.nombre


class Localidad(CommonStruct):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    cod_postal = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.nombre


class Domicilio(CommonStruct):
    TIPO = (('Av.', 'Avenida'), ('Calle', 'Calle'), ('Pje.', 'Pasaje'))
    
    tipo = models.CharField(max_length=5, choices=TIPO, default='Calle')
    calle = models.CharField(max_length=40)
    numero = models.IntegerField('Número', null=True, blank=True)
    piso = models.CharField(max_length=2, null=True, blank=True)
    puerta = models.CharField(max_length=2, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    # configuración para admin
    list_display = ['id', 'tipo', 'calle', 'numero', 'piso', 'puerta']
    list_display_links = ['id']
    exclude = []
    search_fields = ['calle']
    list_filter = ['ciudad', 'localidad']
    date_hierarchy = ''

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return "%s %s" % (self.calle, self.numero)

    def get_absolute_url(self):
        # reverse('comunes:domi_info', kwargs={'pk': self.pk})
        return reverse('comunes:diccionario_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('comunes:domdiccionario_update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comunes:diccionario_delete', args=(self.pk,))


class Diccionario(CommonStruct):
    TABLA = (('actividad', 'Actividades'), ('domicilio', 'Domicilios'),)

    texto = models.CharField(max_length=150)
    tabla = models.CharField(max_length=45, choices=TABLA, default='actividad')

    class Meta:
        verbose_name = 'Diccionario'
        verbose_name_plural = 'Diccionarios'

    def __str__(self):
        return "%s (%s)" % (self.texto, self.get_tabla_display())

    def get_texto(self):
        return str(self.texto).capitalize()

    def get_absolute_url(self):
        return reverse('comunes:diccionario_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('comunes:diccionario_update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comunes:diccionario_delete', args=(self.pk,))


class Comunicacion(CommonStruct):
    TIPO = (('tel', 'Teléfono'), ('movil', 'Celular'), ('wa', 'WhatsApp'),
            ('email', 'Correo Electrónico'), ('face', 'Facebook'),
            ('twitt', 'Twitter'), ('link', 'LinkedIn'))

    tipo = models.CharField(max_length=5, choices=TIPO, default='movil')
    texto = models.CharField(max_length=150)

    # configuración para admin
    list_display = ['id', 'tipo', 'texto']
    list_display_links = ['id']
    exclude = []
    search_fields = []
    list_filter = []
    date_hierarchy = ''

    class Meta:
        verbose_name = 'Comunicacion'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return "%s: %s" % (self.get_tipo_display(), self.texto)

    def get_absolute_url(self):
        return reverse('comunes:comunicacion_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('comunes:comunicacion_update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comunes:comunicacion_delete', args=(self.pk,))
