from . import views
from django.urls import path
from .views import ServicesView, CaseStudyView

urlpatterns = [
    path('', views.ServicesView, name='services'),
]