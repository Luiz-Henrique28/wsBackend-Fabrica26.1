from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('jogar/', views.jogar, name='jogar'),
    path('pergunta/', views.pergunta, name='pergunta'),
    path('responder/', views.responder, name='responder'),
    path('resultado/', views.resultado, name='resultado'),
]
