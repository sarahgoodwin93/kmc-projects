from django import forms
from .models import Services


class AddServiceForm(forms.ModelForm):
    """
    FORM: Add Services.
    """

    class Meta:
        model = Services
        fields = [
            "name",
            "description",
        ]
