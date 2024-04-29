from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Services, CaseStudy
from .forms import AddServiceForm, EditServiceForm, AddCaseStudyForm, EditCaseStudyForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test


# Services List
def ServiceList(request):
    """
    Returns services list in :model:`services.Services``
    and displays them to the services page.
    Returns case study list in :model:`services.CaseStudy``
    and displays them to the services page.
    """
    services = Services.objects.all()
    casestudies = CaseStudy.objects.all()
    return render(request, 'services/services.html', {'services': services, 'casestudies': casestudies})


# Check SuperUser
def is_superuser(user):
    """
    Check if the user is a superuser.
    """
    return user.is_authenticated and user.is_superuser


# Add Services View
class AddServiceView(UserPassesTestMixin, CreateView):
    """
    Show the add service page so that a superuser can add a new service
    to the site. Once a service has been added the page will redirect to
    the services page so the new service can be viewed.
    Tests if the user is a superuse
    """
    model = Services
    template_name = "services/add_service.html"
    form_class = AddServiceForm
    success_url = reverse_lazy("services")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for adding a new service")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Add Service")
        )
    
    def test_func(self):
        return self.request.user.is_superuser


# Edit Services View
class EditServiceView(UserPassesTestMixin, UpdateView):
    """
    Shows the edit services page so that a superuser can edit
    the servicess, once the user has edited the service sucssefully it will
    redirect back to the services using the success_url
    """
    model = Services
    template_name = "services/edit_service.html"
    form_class = EditServiceForm
    success_url = reverse_lazy("services")

    def swim_edit(self, request):
        messages.success(self, request, "Service has been updated")
        return response

    def test_func(self):
        return self.request.user.is_superuser


# Delete Service View
class DeleteServiceView(UserPassesTestMixin, DeleteView):
    """
    Shows the delete service page so that the superuser can delete a service.
    Once the service has been delete it will redirect back
    to the services using the success_url
    """

    model = Services
    template_name = "services/delete_service.html"
    success_url = reverse_lazy("services")

    def swim_delete(self, request):
        messages.success(self, request, "Service has been deleted")
        return super().delete(request)

    def test_func(self):
        return self.request.user.is_superuser


# Add Case Study View
class AddCaseStudyView(UserPassesTestMixin, CreateView):
    """
    Show the add case study page so that a superuser can add a new case study
    to the site. Once a case study has been added the page will redirect to
    the services page so the new case study can be viewed.
    """
    model = Services
    template_name = "services/add_casestudy.html"
    form_class = AddCaseStudyForm
    success_url = reverse_lazy("services")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for adding a new case study")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Add Case Study")
        )

    def test_func(self):
        return self.request.user.is_superuser


# Edit Case Study View
class EditCaseStudyView(UserPassesTestMixin, UpdateView):
    """
    Shows the edit case study page so that a superuser can edit
    the case study, once the user has edited the case study sucssefully it will
    redirect back to the services using the success_url
    """
    model = CaseStudy
    template_name = "services/edit_casestudy.html"
    form_class = EditCaseStudyForm
    success_url = reverse_lazy("services")

    def swim_edit(self, request):
        messages.success(self, request, "Case Study has been updated")
        return response
    
    def test_func(self):
        return self.request.user.is_superuser


# Delete Case Study View
class DeleteCaseStudyView(UserPassesTestMixin, DeleteView):
    """
    Shows the delete case study page so that the superuser can delete a case study.
    Once the service has been deleted it will redirect back
    to the services using the success_url
    """

    model = CaseStudy
    template_name = "services/delete_casestudy.html"
    success_url = reverse_lazy("services")

    def swim_delete(self, request):
        messages.success(self, request, "Case Study has been deleted")
        return super().delete(request)
    
    def test_func(self):
        return self.request.user.is_superuser