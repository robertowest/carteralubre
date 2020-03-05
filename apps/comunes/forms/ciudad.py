from django import forms
from material import Layout, Row

from apps.comunes.models.ciudad import Ciudad

class CiudadForm(forms.ModelForm):
    layout = Layout(
        Row('pais'),
        Row('nombre', 'cod_area_tel'),
    )

    class Meta:
        model = Ciudad
        fields = ['pais', 'nombre', 'cod_area_tel', 'active']