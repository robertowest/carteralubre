from datetime import datetime
from django.db import models

# Create your models here.
class AudtoriaMixin(models.Model):
    active = models.BooleanField('Activo', default=True)
    created = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True, blank=True)
    created_by = models.CharField('Creado por', max_length=15, editable=False, null=True, blank=True)
    modified = models.DateTimeField('Modificado', auto_now_add=True, editable=False, null=True, blank=True)
    modified_by = models.CharField('Modif. por', max_length=15, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        super(AudtoriaMixin, self).save(*args, **kwargs)

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self):
        super(AudtoriaMixin, self).delete()

    class Meta:
        abstract = True
