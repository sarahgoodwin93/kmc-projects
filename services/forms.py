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
            "price",
        ]


class EditServiceForm(forms.ModelForm):
    """
    FORM: Edit Services.
    """

    class Meta:
        model = Services
        fields = [
            "name",
            "description",
            "price",
        ]