from django import forms
from material import Layout, Row

from apps.comunes.models.domicilio import Domicilio

class DomicilioForm(forms.ModelForm):
    layout = Layout(
        Row('tipo', 'calle'),
        Row('numero', 'piso', 'puerta'),
        Row('pais'),
        Row('ciudad'),
        Row('localidad'),
        'active',
    )

    class Meta:
        model = Domicilio
        fields = ['tipo', 'calle', 'numero', 'piso', 'puerta',
                  'pais', 'ciudad', 'localidad',
                  'active']
