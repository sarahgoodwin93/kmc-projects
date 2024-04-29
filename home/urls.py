from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    ContactFormView,
    ContactListView,
    NewsletterView,
)

urlpatterns = [
    path('', views.index, name='home'),
    path('home/contact', ContactFormView.as_view(), name='contact'),
    path('home/contact/list', views.ContactListView, name='contact_list'),
    path('home/newsletter', NewsletterView.as_view(), name='newsletter'),
]