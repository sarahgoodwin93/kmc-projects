from django import forms
from .models import Order

"""
The base of this code was taken and modified from the walkthrough
project Boutiuqe Ado > The Checkout App > Admin, Signals & Forms Part 2.
Additional code comments have been added to show understanding.
Parts have been removed that were not relevant to this site and some
naming has been changed to better suit KMC Projects.
"""


class OrderForm(forms.ModelForm):
    """
    Form for handling order information.
    """
    class Meta:
        """
        Defines metadata for the form.
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',)
        
    def __init__(self, *args, **kwargs):
        """
        Customizes the form's initialization.
        Sets placeholders and autofocus to start on the full name field.
        Iterates through the form adding a star to the placeholder if the
        field is required.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
        }

        # Set autofocus on the full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Iterate through fields to set placeholders, add star if required
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


