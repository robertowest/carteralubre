from django import forms
from material import Layout, Row

from apps.comunes.models.comunicacion import Comunicacion

class ComunicacionForm(forms.ModelForm):
    layout = Layout(
        Row('tipo', 'texto'),
        'active',
    )

    class Meta:
        model = Comunicacion
        fields = ['tipo', 'texto', 'active']
