from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('write/', views.write, name='write'),
    path('create_people/', views.create_people, name='create_people'),
    path('day/', views.day, name='day'),

]

