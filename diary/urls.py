from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('write/', views.write, name='write')
]

