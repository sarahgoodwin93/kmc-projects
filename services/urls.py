from django.urls import path
from . import views
from .views import (
    ServiceList,
    AddServiceView,
)

urlpatterns = [
    path('', views.ServiceList, name='services'),
    path("services/add/", AddServiceView.as_view(), name="add_service"),
]
