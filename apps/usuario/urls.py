from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'usuario'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    # template_name='startup/login.html'
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'),
         name='reset_password'),

    # registro y perfil de usuario
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
