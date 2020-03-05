from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.comunes.forms.domicilio import Domicilio, DomicilioForm

PAGINATION = 15


class ListView(ListView):
    model = Domicilio
    template_name = 'domicilio/listado.html'
    paginate_by = PAGINATION


class NewView(CreateView):
    model = Domicilio
    template_name = 'domicilio/formulario.html'
    form_class = DomicilioForm


class DetailView(DetailView):
    model = Domicilio
    template_name = 'domicilio/info.html'


class UpdateView(UpdateView):
    model = Domicilio
    template_name = 'domicilio/formulario.html'
    form_class = DomicilioForm


class DeleteView(DeleteView):
    model = Domicilio

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('comunes:domi_listado')
