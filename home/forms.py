from django import forms
from .models import Contact, WhoWeAre


# Contact form for businesses to register intrest.
class ContactForm(forms.ModelForm):
    """
    FORM: Contact.
    """

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "service_needed",
            "message",
        ]


class EditWhoWeAreForm(forms.ModelForm):
    """
    FORM: Edit Who we Are.
    """

    class Meta:
        model = WhoWeAre
        fields = [
            "name",
            "description",
        ]

