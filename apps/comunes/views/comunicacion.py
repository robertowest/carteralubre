from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.comunes.forms.comunicacion import Comunicacion, ComunicacionForm

PAGINATION = 15


class ListView(ListView):
    model = Comunicacion
    template_name = 'comunicacion/listado.html'
    paginate_by = PAGINATION


class NewView(CreateView):
    model = Comunicacion
    template_name = 'comunicacion/formulario.html'
    form_class = ComunicacionForm


class DetailView(DetailView):
    model = Comunicacion
    template_name = 'comunicacion/info.html'


class UpdateView(UpdateView):
    model = Comunicacion
    template_name = 'comunicacion/formulario.html'
    form_class = ComunicacionForm


class DeleteView(DeleteView):
    model = Comunicacion

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('comunes:comu_listado')
