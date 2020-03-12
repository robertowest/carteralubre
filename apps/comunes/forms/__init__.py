from .domicilio import *
from .pais import *
from .ciudad import *
from .localidad import *

from .comunicacion import *

from django import forms

class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
