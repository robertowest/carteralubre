from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
def home(request):
    return render(request, 'base.html', context={},)


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


class PersonaCreateView(generic.CreateView):
    pass


class PersonaUpdateView(generic.UpdateView):
    pass


class PersonaDeleteView(generic.DeleteView):
    pass
