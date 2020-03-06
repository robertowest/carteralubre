from django.urls import path

from apps.comunes.views import comunicacion, diccionario, domicilio

app_name = __package__.split('.')[1]

# urlpatterns = [
#     # comunicaciones
#     path('comunicacion/', comunicacion.ListView.as_view(), name='comunicacion_list'),
#     path('comunicacion/crear/', comunicacion.CreateView.as_view(), name='comunicacion_create'),
#     path('comunicacion/<int:pk>/', comunicacion.DetailView.as_view(), name='comunicacion_detail'),
#     path('comunicacion/<int:pk>/modificar/', comunicacion.UpdateView.as_view(), name='comunicacion_update'),
#     path('comunicacion/<int:pk>/eliminar/', comunicacion.DeleteView.as_view(), name='comunicacion_delete'),

#     # diccionario
#     path('diccionario/', diccionario.ListView.as_view(), name='diccionario_list'),

#     # domicilios
#     path('domicilio/', domicilio.ListView.as_view(), name='domicilio_list'),
#     path('domicilio/crear/', domicilio.CreateView.as_view(), name='domicilio_create'),
#     path('domicilio/<int:pk>/', domicilio.DetailView.as_view(), name='domicilio_detail'),
#     path('domicilio/<int:pk>/modificar/', domicilio.UpdateView.as_view(), name='domicilio_update'),
#     path('domicilio/<int:pk>/eliminar/', domicilio.DeleteView.as_view(), name='domicilio_delete'),
# ]
