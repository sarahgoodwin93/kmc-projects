from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Contact, NewsletterSignUp
from .forms import ContactForm, NewsLetterForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


class ContactFormView(CreateView):
    """ A view to return the contact page """
    model = Contact
    template_name = "home/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for contacting us")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Contact")
        )


def ContactListView(request):
    """ A view to show the admin a list of who has contacted them """
    contact = Contact.objects.all()
    return render(request, 'home/contact_list', {'contact': contact})


class NewsletterView(CreateView):
    """ A view to return the newsletter signup page """
    model = NewsletterSignUp
    template_name = "home/newsletter-signup.html"
    form_class = NewsLetterForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for signing up to our newsletter")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Newsletter")
        )
