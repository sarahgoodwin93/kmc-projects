from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserDetails
from .forms import UserDetailsForm


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