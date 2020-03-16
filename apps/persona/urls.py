from django.urls import path
from . import views

app_name = __package__.split('.')[1]

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.PersonaTemplateView.as_view(), name='index'),
    path('listado/', views.PersonasListView.as_view(), name='list'),
    path('crear/', views.PersonaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PersonaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.PersonaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='delete'),
]
