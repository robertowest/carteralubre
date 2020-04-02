from django.urls import path
from apps.empresa import views

app_name = 'actividad'

urlpatterns = [
    path('', views.ActividadTemplateView.as_view(), name='index'),
    path('listado/', views.ActividadListView.as_view(), name='list'),
    path('crear/', views.ActividadCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ActividadDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.ActividadUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ActividadDeleteView.as_view(), name='delete'),
]
