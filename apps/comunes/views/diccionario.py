from django.views.generic import ListView

from apps.comunes.forms.diccionario import Diccionario

PAGINATION = 15


class ListView(ListView):
    model = Diccionario
    template_name = 'diccionario/listado.html'
    paginate_by = PAGINATION
