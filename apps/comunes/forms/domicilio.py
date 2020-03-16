from crispy_forms import helper, layout
from django import forms

from apps.comunes.models import Domicilio as DomicilioModel


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = DomicilioModel
        fields = ['tipo', 'calle', 'numero', 'piso', 'puerta', 'pais', 'ciudad', 'localidad', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['actividad'].queryset = Diccionario.objects.filter(tabla='actividad')
        self.helper = helper.FormHelper()
        self.helper.layout = layout.Layout(
            'tipo', 
            'calle', 
            'numero', 
            'piso', 
            'puerta', 
            'pais', 
            'ciudad', 
            'localidad', 
            'active'
        )
        self.helper.layout.append(
            layout.HTML('<button type="submit" class="btn btn-primary btn-icon-split">'
                        '<span class="icon text-white-50">'
                        '<i class="fas fa-save"></i>'
                        '</span>'
                        '<span class="text">Grabar</span>'
                        '</button>')
        )
