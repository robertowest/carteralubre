from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.domicilio import DomicilioForm

# 
# Domicilio
#  
class DomicilioTemplateView(TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return DomicilioListView.as_view()(request)


class DomicilioListView(ListView):
    model = DomicilioModel
    template_name = 'comunes/tabla.html'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = DomicilioModel.objects.filter(active=True)
        return context
 
 
class DomicilioCreateView(CreateView):
    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'
    success_url = reverse_lazy('{app}:list'.format(app=__package__.split('.')[1]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Domicilio'
        return context
        
    def form_valid(self, form):
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response
 
 
class DomicilioDetailView(DetailView):
    model = DomicilioModel
    template_name = 'comunes/detalle.html'
 
 
class DomicilioUpdateView(UpdateView):
    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificación de Domicilio'
        return context

    def form_valid(self, form):
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response

 
class DomicilioDeleteView(DeleteView):
    pass