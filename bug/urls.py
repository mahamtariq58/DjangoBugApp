from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name = 'index'),
    path('register_bug', views.register_bug, name ='register_bug'),
    path('bug/<int:bug_id>', views.fields_bug, name = 'fields_bug')

]