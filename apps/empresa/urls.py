from django.urls import path
from . import views

app_name = __package__.split('.')[1]

urlpatterns = [
    # index es la página principal de la app
    # list es el listado de la tabla, si no hay página principal, convertimos list en index

    # path('', views.EmpresaTemplateView.as_view(), name='index'),
    # path('listado/', views.EmpresaListView.as_view(), name='list'),

    path('', views.EmpresaListView.as_view(), name='index'),
    path('crear/', views.EmpresaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.EmpresaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='delete'),

]
