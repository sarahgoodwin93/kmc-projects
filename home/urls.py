from django.contrib import admin
from django.urls import path
from . import views
from newsletter.views import NewsletterView
from .views import (
    ContactFormView,
    ContactListView,
)

urlpatterns = [
    path('', views.index, name='home'),
    path('home/contact/', ContactFormView.as_view(), name='contact'),
    path('home/contact/list/', ContactListView.as_view(), name='contact_list'),
]
