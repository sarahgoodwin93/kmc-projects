from django.urls import path
from . import views
from .views import orders

urlpatterns = [
    path('', views.orders, name='orders')
]