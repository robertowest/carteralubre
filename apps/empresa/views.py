from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy, resolve
from django.views import generic

from . import models


class EmpresaTemplateView(generic.TemplateView):
    model = models.Empresa
    template_name = '{app}/index.html'.format(app=model._meta.verbose_name.lower())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['actividades'] = self.model.objects.values('actividad', 'actividad__texto').annotate(contador=Count(id))
        context['comerciales'] = self.model.objects.values('comercial', 'comercial__persona__apellido').annotate(contador=Count(id))
        return context


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


# class EmpresaCreateView(LoginRequiredMixin, generic.CreateView):
class EmpresaCreateView(generic.CreateView):
    model = models.Empresa
    # fields = '__all__'
    fields = ['razon_social', 'cuit', 'domicilios', 'comunicaciones', 'comercial', 'actividad', 'active']
    template_name = '{app}/create.html'.format(app=model._meta.verbose_name.lower())

    def get_success_url(self):

        return reverse_lazy('empresa:index')
        
    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class EmpresaUpdateView(generic.UpdateView):
    model = models.Empresa
    # fields = '__all__'
    fields = ['razon_social', 'cuit', 'domicilios', 'comunicaciones', 'comercial', 'actividad', 'active']
    template_name = '{app}/form.html'.format(app=model._meta.verbose_name.lower())


class EmpresaDeleteView(generic.DeleteView):
    pass


class FilterListView(generic.ListView):
    model = models.Empresa
    template_name = '{app}/list.html'.format(app=model._meta.verbose_name.lower())
    paginate_by = 15

    def url_name(self):
        attrib = resolve(self.request.path)
        return getattr(attrib, 'url_name', 'all')

    def get_queryset(self):
        # attrib = resolve(self.request.path)
        # name = getattr(attrib, 'url_name', 'all')
        name = self.url_name()
        if self.kwargs['filtro'] == 0:
            self.kwargs['filtro'] = None

        if name == 'filtro_actividad':
            return self.model.objects.filter(actividad=self.kwargs['filtro'])
        if name == 'filtro_comercial':
            return self.model.objects.filter(comercial=self.kwargs['filtro'])
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.url_name()
        if name == 'filtro_actividad':
            context['filtro'] = 'filtrado por Actividad'
        if name == 'filtro_comercial':
            context['filtro'] = 'filtrado por Comercial'
        return context
