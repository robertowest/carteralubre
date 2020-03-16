from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.domicilio import DomicilioForm

# 
# Domicilio
#  
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('{app}:list'.format(app=__package__.split('.')[1]))
        
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
 
 
class DomicilioDetailView(DetailView):
    model = DomicilioModel
    template_name = 'comunes/detalle.html'
 
 
class DomicilioUpdateView(UpdateView):
    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'

    def get_success_url(self):
        name = self.model._meta.verbose_name.lower()
        return reverse_lazy('{app}:list'.format(app=name))
 
 
class DomicilioDeleteView(DeleteView):
    pass