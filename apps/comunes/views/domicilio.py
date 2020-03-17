from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.domicilio import DomicilioForm


import re

def get_referer_view(request, default=None):
    ''' 
    Return the referer view of the current request

    Example:

        def some_view(request):
            ...
            referer_view = get_referer_view(request)
            return HttpResponseRedirect(referer_view, '/accounts/login/')
    '''

    # if the user typed the url directly in the browser's address bar
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return default

    # remove the protocol and split the url at the slashes
    referer = re.sub('^https?:\/\/', '', referer).split('/')
    if referer[0] != request.META.get('SERVER_NAME'):
        return default

    # add the slash at the relative path's view and finished
    referer = u'/' + u'/'.join(referer[1:])
    return referer


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
        response = super().form_valid(form)
        return response
 
 
class DomicilioDetailView(DetailView):
    model = DomicilioModel
    template_name = 'comunes/detalle.html'
 
 
class DomicilioUpdateView(UpdateView):
    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'
    # success_url = get_referer_view(UpdateView.model)
    # self.request.META.HTTP_REFERER

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificación de Domicilio'
        return context

    def get_success_url(self):
        name = get_referer_view(self.request)
        name = self.model._meta.verbose_name.lower()
        return reverse_lazy('{app}:list'.format(app=name))

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

 
class DomicilioDeleteView(DeleteView):
    pass