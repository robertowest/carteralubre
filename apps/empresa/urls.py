from django.urls import path
from . import views

app_name = __package__.split('.')[1]

urlpatterns = [
    path('', views.EmpresaTemplateView.as_view(), name='index'),
    path('listado/', views.EmpresaListView.as_view(), name='list'),
    path('crear/', views.EmpresaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.EmpresaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='delete'),

    path('filtro_actividad/<int:filtro>', views.FilterListView.as_view(), name='filtro_actividad'),
    path('filtro_comercial/<int:filtro>', views.FilterListView.as_view(), name='filtro_comercial'),
]







from django.shortcuts import render
def muestra(request):
    return render(request, 'base.html', context={},)

urlpatterns += [
    path('base/', muestra, name='base'),
]
