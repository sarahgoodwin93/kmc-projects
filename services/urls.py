from django.urls import path
from . import views
from .views import (
    ServiceList,
    AddServiceView,
    EditServiceView,
)

urlpatterns = [
    path('', views.ServiceList, name='services'),
    path("services/add/", AddServiceView.as_view(), name="add_service"),
    path("services/edit/<int:pk>/", EditServiceView.as_view(), name="edit_service"),
]
