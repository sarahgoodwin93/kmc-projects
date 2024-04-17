from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceList, name='services'),
]
