from crispy_forms import helper, layout
from django import forms

from apps.comunes.models import Diccionario
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'razon_social', 'cuit', 'comercial', 'actividad', 'referencia_id', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['actividad'].queryset = Diccionario.objects.filter(tabla='actividad')
        self.helper = helper.FormHelper()
        self.helper.layout = layout.Layout(
            'nombre', 'razon_social', 'cuit', 'comercial', 'actividad', 'referencia_id', 'active'
        )
        self.helper.layout.append(
            layout.HTML('<button type="submit" class="btn btn-primary btn-icon-split">'
                        '<span class="icon text-white-50">'
                        '<i class="fas fa-save"></i>'
                        '</span>'
                        '<span class="text">Grabar</span>'
                        '</button>')
        )
