from django import forms
from .models import Services, CaseStudy


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


class EditServiceForm(forms.ModelForm):
    """
    FORM: Edit Services.
    """

    class Meta:
        model = Services
        fields = [
            "name",
            "description",
        ]

class AddCaseStudyForm(forms.ModelForm):
    """
    FORM: Add Services.
    """

    class Meta:
        model = CaseStudy
        fields = [
            "title",
            "body",
            "image",
        ]


class EditCaseStudyForm(forms.ModelForm):
    """
    FORM: Edit Services.
    """

    class Meta:
        model = CaseStudy
        fields = [
            "title",
            "body",
            "image",
        ]