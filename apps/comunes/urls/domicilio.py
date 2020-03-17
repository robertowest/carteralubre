from django.urls import path
from apps.comunes.views import domicilio as views

app_name = 'domicilio'

urlpatterns = [
    path('', views.DomicilioTemplateView.as_view(), name='index'),
    path('listado/', views.DomicilioListView.as_view(), name='list'),
    path('crear/', views.DomicilioCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DomicilioDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.DomicilioUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DomicilioDeleteView.as_view(), name='delete'),
]