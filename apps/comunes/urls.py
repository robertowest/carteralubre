from django.urls import path

from apps.comunes.views import comunicacion, diccionario, domicilio

app_name = 'comunes'

urlpatterns = [
    # comunicaciones
    path('comunicacion/', comunicacion.ListView.as_view(), name='comu_listado'),
    path('comunicacion/nuevo/', comunicacion.NewView.as_view(), name='comu_nuevo'),
    path('comunicacion/info/<int:pk>/', comunicacion.DetailView.as_view(), name='comu_info'),
    path('comunicacion/modif/<int:pk>/', comunicacion.UpdateView.as_view(), name='comu_modif'),
    path('comunicacion/borrar/<int:pk>/', comunicacion.DeleteView.as_view(), name='comu_borrar'),

    # diccionario
    path('diccionario/', diccionario.ListView.as_view(), name='dicc_listado'),

    # domicilios
    path('domicilio/', domicilio.ListView.as_view(), name='domi_listado'),
    path('domicilio/nuevo/', domicilio.NewView.as_view(), name='domi_nuevo'),
    path('domicilio/info/<int:pk>/', domicilio.DetailView.as_view(), name='domi_info'),
    path('domicilio/modif/<int:pk>/', domicilio.UpdateView.as_view(), name='domi_modif'),
    path('domicilio/borrar/<int:pk>/', domicilio.DeleteView.as_view(), name='domi_borrar'),
]