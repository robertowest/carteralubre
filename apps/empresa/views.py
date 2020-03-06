from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import models


class EmpresaTemplateView(generic.TemplateView):
    pass


class EmpresaListView(generic.ListView):
    model = models.Empresa
    template_name = '{app}/list.html'.format(app=model._meta.verbose_name.lower())
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = models.Empresa.objects.filter(active=True)
        return context


class EmpresaDetailView(generic.DetailView):
    model = models.Empresa
    template_name = '{app}/detail.html'.format(app=model._meta.verbose_name.lower())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domicilios'] = context['empresa'].domicilios.filter(active=True)
        context['comunicaciones'] = context['empresa'].comunicaciones.filter(active=True)
        return context


class EmpresaCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Empresa
    # fields = '__all__'
    fields = ['razon_social', 'cuit', 'domicilios', 'comunicaciones', 'comercial', 'actividad', 'active']
    template_name = '{app}/create.html'.format(app=model._meta.verbose_name.lower())

    def get_success_url(self):
        return reverse_lazy('Empresa:index')
        
    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class EmpresaUpdateView(generic.UpdateView):
    pass


class EmpresaDeleteView(generic.DeleteView):
    pass
