from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import NewsLetterForm

def NewsletterView(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            send_confirmation_email(form.cleaned_data['email'])
            messages.success(request, "Thank you for signing up for our newsletter!")
            return redirect(reverse('home')) 
    else:
        form = NewsLetterForm()

    return render(request, 'newsletter/newsletter-signup.html', {'form': form})

def send_confirmation_email(email):
    subject_template_name = 'Thanks for signing up'
    email_template_name = 'newsletter/confirmation_email_body.txt'
    context = {'email': email}
    
    subject = render_to_string(subject_template_name, context).strip()
    email_body = render_to_string(email_template_name, context)

    send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, [email])
