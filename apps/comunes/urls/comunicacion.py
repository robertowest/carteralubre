from django.urls import path
from apps.comunes.views import comunicacion as views

app_name = 'comunicacion'

urlpatterns = [
    path('', views.ComunicacionTemplateView.as_view(), name='index'),
    path('listado/', views.ComunicacionListView.as_view(), name='list'),
    path('crear/', views.ComunicacionCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ComunicacionDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.ComunicacionUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ComunicacionDeleteView.as_view(), name='delete'),
]