# from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import resolve
from django.views import generic

from . import forms, models

from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.comunicacion import ComunicacionForm
from apps.comunes.forms.domicilio import DomicilioForm

from apps.persona.models import Persona as ContactoModel
from apps.persona.forms import PersonaForm as ContactoForm


# -----------------------------------------------------------------------------
# Empresas
# -----------------------------------------------------------------------------


class EmpresaTemplateView(generic.TemplateView):
    # app=__package__.split('.')[1]     --> lo obtiene de urls.py
    # model._meta.verbose_name.lower()  --> lo obtiene de models.py
    model = models.Empresa
    template_name = '{app}/index.html'.format(app=__package__.split('.')[1])

    def get_context_data(self, **kwargs):
        model = self.model
        context = super().get_context_data(**kwargs)
        context['actividades'] = model.objects.values('actividad', 'actividad__nombre').annotate(contador=Count('id'))
        context['comerciales'] = model.objects.values('comercial', 'comercial__persona__apellido').annotate(contador=Count('id'))
        return context


class EmpresaListView(generic.ListView):
    model = models.Empresa
    # template_name = 'comunes/tabla.html'    # .format(app=__package__.split('.')[1])
    template_name = 'empresa/tabla_filtro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = __package__.split('.')[1]
        # context['object_list'] = models.Empresa.objects.filter(active=True)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search1') 
        if search:
            return qs.filter(nombre__icontains=search)
        else: 
            return qs.filter(id=0)


class EmpresaCreateView(generic.CreateView):    # LoginRequiredMixin
    model = models.Empresa
    form_class = forms.EmpresaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Empresa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_name'] = __package__.split('.')[1]
        context['form_title'] = self.form_title
        return context

    # def get_success_url(self):
    #     name = self.model._meta.verbose_name.lower()
    #     return reverse_lazy('{app}:detail'.format(app=name), args=(self.object.pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class EmpresaDetailView(generic.DetailView):
    model = models.Empresa
    template_name = 'empresa/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domicilios'] = context['empresa'].domicilios.filter(active=True)
        context['comunicaciones'] = context['empresa'].comunicaciones.filter(active=True)
        context['contactos'] = context['empresa'].contactos.filter(active=True)
        context['actividades'] = context['empresa'].actividades.filter(active=True)
        # context['empresa'].contactos.filter(tipo='movil').filter(active=True)
        # cargamos los celulares de los contactos
        # for reg in context['contactos']:
        #     reg.comunicaciones = reg.comunicaciones.filter(tipo='movil').filter(active=True)
        return context


class EmpresaUpdateView(generic.UpdateView):
    model = models.Empresa
    form_class = forms.EmpresaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Empresa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    # def get_success_url(self):
    #     name = self.model._meta.verbose_name.lower()
    #     # return reverse_lazy('{app}:detail'.format(app=name), args=(self.kwargs['pk'],))
    #     return reverse_lazy('{app}:detail'.format(app=name), args=(self.object.pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class EmpresaDeleteView(generic.DeleteView):
    pass


# -----------------------------------------------------------------------------
# Empresas filtradas por Actividades y Comerciales
# -----------------------------------------------------------------------------


class FilterListView(generic.ListView):
    model = models.Empresa
    # template_name = '{app}/list.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/tabla.html'

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


# -----------------------------------------------------------------------------
# Tablas relacionadas a la Empreda
# -----------------------------------------------------------------------------


class CreateComunicationView(generic.CreateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Tipo de Comunicación'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        empresa = models.Empresa.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        empresa.comunicaciones.add(self.object)
        
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class CreateAddressView(generic.CreateView):
    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Domicilio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        empresa = models.Empresa.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        empresa.domicilios.add(self.object)

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class CreateContactView(generic.CreateView):
    model = ContactoModel
    form_class = ContactoForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Contacto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        empresa = models.Empresa.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        empresa.contactos.add(self.object)

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class CreateActividadView(generic.CreateView):
    model = models.Actividad
    form_class = forms.ActividadForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Subactividad'

    def get_context_data(self, **kwargs):
        context = super(CreateActividadView, self).get_context_data(**kwargs)        
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        empresa = models.Empresa.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        empresa.actividades.add(self.object)

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


# -----------------------------------------------------------------------------
# Actividad
# -----------------------------------------------------------------------------

class ActividadTemplateView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return ActividadListView.as_view()(request)


class ActividadListView(generic.ListView):
    model = models.Actividad
    template_name = 'comunes/tabla.html'

    def get_queryset(self):
        # queryset = super().get_queryset()
        # sql = "SELECT id, nombre, parent_id FROM empresa_actividad ORDER BY case when parent_id is null then id else parent_id end * 1000 + id ASC"
        # queryset = models.Actividad.objects.raw(sql).all()
        # return queryset
        ordering = 'CASE WHEN parent_id IS Null THEN id ELSE parent_id END * 1000 + id'
        qs = models.Actividad.objects.all().extra(select={'criterio': ordering}, order_by=('criterio',))
        return qs


class ActividadCreateView(generic.CreateView):
    model = models.Actividad
    form_class = forms.ActividadForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Actividad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class ActividadDetailView(generic.DetailView):
    model = models.Actividad
    template_name = 'comunes/detalle.html'


class ActividadUpdateView(generic.UpdateView):
    model = models.Actividad
    form_class = forms.ActividadForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Actividad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class ActividadDeleteView(generic.DeleteView):
    pass
