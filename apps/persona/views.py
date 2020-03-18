from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import forms, models
from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.forms.comunicacion import ComunicacionForm


# Create your views here.
def home(request):
    # return render(request, 'base.html', context={},)
    return render(request, 'ejemplos/register.html', context={},)


class PersonaTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return PersonasListView.as_view()(request)


class PersonasListView(generic.ListView):
    model = models.Persona
    template_name = 'comunes/tabla.html'.format(app=__package__.split('.')[1])
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = __package__.split('.')[1]
        context['model_name'] = models.Persona._meta.verbose_name_plural.title()
        context['object_list'] = models.Persona.objects.filter(active=True)
        return context


class PersonaCreateView(generic.CreateView):  # LoginRequiredMixin
    model = models.Persona
    form_class = forms.PersonaForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = __package__.split('.')[1]
        return context

    def get_success_url(self):
        return reverse_lazy('{app}:list'.format(app=__package__.split('.')[1]))
        
    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class PersonaDetailView(generic.DetailView):
    model = models.Persona
    # template_name = 'comunes/detalle.html'
    template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = context['persona'].comunicaciones.filter(active=True)
        return context


class PersonaUpdateView(generic.UpdateView):
    model = models.Persona
    form_class = forms.PersonaForm
    template_name = 'comunes/formulario.html'

    def get_success_url(self):
        return reverse_lazy('{app}:list'.format(app=self.model._meta.verbose_name.lower()))


class PersonaDeleteView(generic.DeleteView):
    pass


class CreateContactView(generic.CreateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, **kwargs):
        # context['view'].kwargs['fk']
        context = super().get_context_data(**kwargs)
        # context['app_name'] = __package__.split('.')[1]
        return context

    def get_success_url(self):
        # {{ request.META.HTTP_REFERER }}
        # return self.request.META.HTTP_REFERER
        return reverse_lazy('{app}:list'.format(app=__package__.split('.')[1]))

    def form_valid(self, form):
        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        persona = models.Persona.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        persona.comunicaciones.add(self.object)
        # terminamos
        return super().form_valid(form)


class CreateAddressView(generic.CreateView):
    pass
