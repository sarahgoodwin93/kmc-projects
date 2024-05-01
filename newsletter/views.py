from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import NewsLetterForm


# Newletter view with email confrimation
class NewsletterView(View):
    """ Newsletter form sign up """
    def get(self, request):
        form = NewsLetterForm()
        return render(request, 'newsletter/newsletter-signup.html', {'form': form})  # noqa

    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            new_newsletter_signup = form.save()
            send_confirmation_email(new_newsletter_signup)
            messages.success(request, "Thank you for signing up for our newsletter!")  # noqa
            return redirect(reverse('home'))
        return render(request, 'newsletter/newsletter-signup.html', {'form': form})  # noqa


def send_confirmation_email(newsletter_signup):
    """
    Sends a confirmation email to the new newsletter subscriber.
    """
    subject = 'newsletter/email_confrimations/newsletter_confirmation.txt'
    email_template_name = 'newsletter/email_confrimations/newsletter-subject.txt'  # noqa
    context = {'email': newsletter_signup.email}
    email_body = render_to_string(email_template_name, context)
    send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, [newsletter_signup.email])  # noqa
