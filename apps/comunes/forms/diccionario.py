from django import forms
from material import Layout, Row

from apps.comunes.models.diccionario import Diccionario

class DiccionarioForm(forms.ModelForm):
    layout = Layout(
        Row('tabla', 'texto'),
        'active',
    )

    class Meta:
        model = Diccionario
        fields = ['tabla', 'texto', 'active']
