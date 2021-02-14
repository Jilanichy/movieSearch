from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('find/', views.find, name='find'),
    path('list', views.movie_list, name='movie_list'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
