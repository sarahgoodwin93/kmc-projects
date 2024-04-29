from django import forms
from .models import Contact, NewsletterSignUp


class ContactForm(forms.ModelForm):
    """
    FORM: Contact.
    """

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "message",
        ]


class NewsLetterForm(forms.ModelForm):
    """
    FORM: Newsletter.
    """

    class Meta:
        model = NewsletterSignUp
        fields = [
            "name",
            "email",
        ]

