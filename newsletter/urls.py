from django.urls import path
from . import views
from .views import NewsletterView

urlpatterns = [
    path('newsletter/', views.NewsletterView, name='newsletter'),
]