from django import forms
from .models import UserDetails

"""
The base of this code was taken and modified from the walkthrough 
project Boutiuqe Ado > The Checkout App > Admin, Signals & Forms Part 2.
Additional code comments have been added to show understanding.
Parts have been removed that were not relevant to this site and some
naming has been changed to better suit KMC Projects.  
"""

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        exclude = ('user',)
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
        }

        self.fields['default_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False