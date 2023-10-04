from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name = 'index'),
    path('register_bug', views.register_bug, name ='register_bug')

]