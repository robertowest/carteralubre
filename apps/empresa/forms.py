from django import forms

from apps.comunes.models import Diccionario
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'razon_social', 'cuit', 'comercial', 'actividad', 'referencia_id', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['actividad'].queryset = Diccionario.objects.filter(tabla='actividad')
