from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import models

# Create your views here.
def home(request):
    # return render(request, 'base.html', context={},)
    return render(request, 'ejemplos/register.html', context={},)


class PersonaTemplateView(generic.TemplateView):
    pass


class PersonasListView(generic.ListView):
    model = models.Persona
    paginate_by = 100  # if pagination is desired    
    template_name = '{app}/list.html'.format(app=__package__.split('.')[1])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = __package__
        context['model_name'] = models.Persona._meta.verbose_name_plural.title()
        context['object_list'] = models.Persona.objects.filter(active=True)
        return context


class PersonaDetailView(generic.DetailView):
    pass


class PersonaCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Persona
    fields = ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'active']
    # template_name = '{app}/create.html'.format(app=__package__.split('.')[1])
    template_name = '{app}/create.html'.format(app=model._meta.verbose_name.lower())

    def get_success_url(self):
        return reverse_lazy('persona:index')    


class PersonaUpdateView(generic.UpdateView):
    pass


class PersonaDeleteView(generic.DeleteView):
    pass
