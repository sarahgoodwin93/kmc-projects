from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.conf import settings


# Homepage View
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# Contact Form View
class ContactFormView(CreateView):
    """ A view to return the contact page """
    model = Contact
    template_name = "home/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user

        # Send email to your inbox
        contact = form.cleaned_data
        send_mail(
            subject=f"New KMC Contact: {contact['name']}",
            message=(
                f"Service Needed: {contact['service_needed']}\n\n"
                f"Message:\n{contact['message']}\n\n"
                f"Email: {contact['email']}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['sarah@lylotechstudio.com', 'kevin@kmcprojects.com.au'],
        )

        messages.success(self.request, "Thanks for contacting us, we'll be in touch soon")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form. Please check your details and try again.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Contact")
        )


# Check SuperUser
def is_superuser(user):
    """
    Check if the user is a superuser.
    """
    return user.is_authenticated and user.is_superuser


# Contact List View
class ContactListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ A view to show the admin a list of who has contacted them """
    model = Contact
    template_name = 'home/contact_list.html'
    context_object_name = 'contacts'

    def test_func(self):
        return self.request.user.is_superuser
