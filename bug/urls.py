from django.urls import path

from . import views

app_name = 'bug'
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path('register_bug', views.register_bug, name ='register_bug'),
    path('bug/<int:pk>/', views.DetailView.as_view(), name = 'detail'),


]