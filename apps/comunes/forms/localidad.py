from django import forms
from material import Layout, Row

from apps.comunes.models.localidad import Localidad

class LocalidadForm(forms.ModelForm):
    layout = Layout(
        Row('ciudad'),
        Row('nombre', 'cod_postal'),
    )

    class Meta:
        model = Localidad
        fields = ['ciudad', 'nombre', 'cod_postal', 'active']