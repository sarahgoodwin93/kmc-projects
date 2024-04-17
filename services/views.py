from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Services, CaseStudy
from .forms import AddServiceForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

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


class AddServiceView(LoginRequiredMixin, CreateView):
    model = Services
    template_name = "services/add_service.html"
    form_class = AddServiceForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for adding a new service")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Add Service")
        )

