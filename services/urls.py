from django.urls import path
from . import views
from .views import (
    ServiceList,
    AddServiceView,
    EditServiceView,
    DeleteServiceView,
    AddCaseStudyView,
    EditCaseStudyView,
    DeleteCaseStudyView,
)

urlpatterns = [
    path('', views.ServiceList, name='services'),
    path("services/add/", AddServiceView.as_view(), name="add_service"),
    path("services/edit/<int:pk>/", EditServiceView.as_view(), name="edit_service"),
    path("services/delete/<int:pk>/", DeleteServiceView.as_view(), name="delete_service"),
    path("services/add/casestudy", AddCaseStudyView.as_view(), name="add_casestudy"),
    path("services/edit/casestudy/<int:pk>/", EditCaseStudyView.as_view(), name="edit_casestudy"),
    path("services/delete/casestudy/<int:pk>/", DeleteCaseStudyView.as_view(), name="delete_casestudy"),
]
