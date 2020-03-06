from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.comunes.forms.comunicacion import Comunicacion, ComunicacionForm

PAGINATION = 15


class ListView(ListView):
    model = Comunicacion
    template_name = '{app}/list.html'.format(app=model._meta.verbose_name.lower())
    paginate_by = PAGINATION


class CreateView(CreateView):
    model = Comunicacion
    template_name = '{app}/create.html'.format(app=model._meta.verbose_name.lower())
    form_class = ComunicacionForm


class DetailView(DetailView):
    model = Comunicacion
    template_name = '{app}/detail.html'.format(app=model._meta.verbose_name.lower())


class UpdateView(UpdateView):
    model = Comunicacion
    template_name = '{app}/update.html'.format(app=model._meta.verbose_name.lower())
    form_class = ComunicacionForm


class DeleteView(DeleteView):
    model = Comunicacion

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('comunes:comunicacion_list')
