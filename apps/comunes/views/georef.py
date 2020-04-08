from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.comunes.models import georef

class PaisListView(ListView):
    model = georef
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(nivel=1)
        return qs


class ProvinciaListView(ListView):
    model = georef
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(nivel=2)
        return qs


class DepartamentoListView(ListView):
    model = georef
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(nivel=3)
        return qs


class MunicipioListView(ListView):
    model = georef
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(nivel=4)
        return qs


class LocalidadListView(ListView):
    model = georef
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(nivel=5)
        return qs
