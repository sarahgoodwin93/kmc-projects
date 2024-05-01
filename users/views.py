from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserDetails
from .forms import UserDetailsForm

"""
The base of this code was taken and modified from the walkthrough 
project Boutiuqe Ado > The Checkout App > Profile App - Part 2.
Additional code comments have been added to show understanding.
Parts have been removed that were not relevant to this site and some
naming has been changed to better suit KMC Projects.  
"""

def UserDetailsView(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserDetails, user=request.user)

    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserDetailsForm(instance=profile)
    orders = profile.user_orders.all()

    template = 'users/users.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)