from crispy_forms import helper, layout
from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.layout = layout.Layout(
            # Row(
            #     Column('nombre', css_class='form-group col-md-6 mb-0'),
            #     Column('apellido', css_class='form-group col-md-6 mb-0'),
            #     css_class='form-row'
            # ),
            'nombre', 
            'apellido',
            'documento',
            'fecha_nacimiento',
            'active'
        )
        # self.helper.add_input(Submit('submit', 'Grabar', css_class='btn-primary'))
        self.helper.layout.append(
            layout.HTML('<button type="submit" class="btn btn-primary btn-icon-split">'
                        '<span class="icon text-white-50">'
                        '<i class="fas fa-save"></i>'
                        '</span>'
                        '<span class="text">Grabar</span>'
                        '</button>')
        )

# <button type="submit" class="btn btn-primary btn-icon-split">
#     <span class="icon text-white-50">
#         <i class="fas fa-save"></i>
#     </span>
#     <span class="text">Grabar</span>
# </button>
