from django.urls import path
from apps.comunes import views

app_name = 'diccionario'

urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('crear/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DeleteView.as_view(), name='delete'),
]