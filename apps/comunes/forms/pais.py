from django import forms
from material import Layout, Row

from apps.comunes.models.pais import Pais

class PaisForm(forms.ModelForm):
    layout = Layout(
        Row('nombre'),
    )

    class Meta:
        model = Pais
        fields = ['nombre', 'active']