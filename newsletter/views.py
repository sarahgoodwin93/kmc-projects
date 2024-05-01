from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import NewsletterSignUp
from .forms import NewsLetterForm
from django.views.generic.edit import CreateView

# Create your views here.
class NewsletterView(CreateView):
    """ A view to return the newsletter signup page """
    model = NewsletterSignUp
    template_name = "newsletter/newsletter-signup.html"
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
