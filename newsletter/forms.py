from django import forms
from .models import NewsletterSignUp


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
