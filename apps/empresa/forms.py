from crispy_forms import helper, layout
from django import forms

from .models import Actividad, Comercial, Empresa


class ActividadForm(forms.ModelForm):
    # multiselect = forms.MultipleChoiceField(
    #                 widget=forms.CheckboxSelectMultiple,
    #                 choices=Actividad.objects.filter(parent__isnull=False).order_by('nombre')
    #               )

    class Meta:
        model = Actividad
        fields = ['nombre', 'parent', 'active'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # valores iniciales para campos especiales
        self.fields['parent'].queryset = Actividad.objects.filter(parent__isnull=True).order_by('nombre')

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts
        self.helper.layout = layout.Layout()        

        # agregamos todos los campos
        for fld in self.Meta.fields:
            self.helper.layout.append(fld)

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'razon_social', 'cuit', 
                  'comercial', 'actividad', 'referencia_id', 'actividades',
                  'observacion', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # valores iniciales para campos especiales
        self.fields['comercial'].queryset = Comercial.objects.all().order_by('persona__nombre')
        self.fields['actividad'].queryset = Actividad.objects.filter(parent__isnull=True).order_by('nombre')

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column('nombre', css_class='col-lg-6 col-md-12 mb-0'),
                layout.Column('razon_social'),
            ),
            layout.Row(
                layout.Column('cuit', css_class='col-lg-3 col-md-3 col-sm-6 mb-0'),
                layout.Column('comercial'),
                layout.Column('referencia_id', css_class='col-lg-3 col-md-3 col-sm-3 mb-0'),
            ),
            layout.Row(
                layout.Column('actividad', css_class='col-lg-6 col-md-12 mb-0'),
                layout.Column('actividades'),
            ),
            'observacion',
        )

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))
