from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.template.loader import render_to_string
from django.core.mail import send_mail


from .forms import OrderForm
from .models import Order, OrderLineItem
from items.models import Item
from users.forms import UserDetailsForm
from users.models import UserDetails
from cart.context import cart_contents

import stripe

"""
The base of this code was taken and modified from the walkthrough
project Boutiuqe Ado > The Checkout App.
Additional code comments have been added to show understanding.
Parts have been removed that were not relevant to this site and some
naming has been changed to better suit KMC Projects.
"""


# Create your views here.
# Order and stripe view
def OrderView(request):
    """
    View for processing orders and handling payment with Stripe.
    """

    # Retrieve Stripe API keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Process order form submission
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart = request.session.get('cart', {})
            for item_id, item_data in cart.items():
                try:
                    item = Item.objects.get(pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Item.DoesNotExist:
                    messages.error(request, "One of the items in your cart wasn't found in our database. Please reach out for assistance!")  # noqa
                    order.delete()
                    return redirect(reverse('cart'))

            # Send confirmation email
            send_confirmation_email(order)

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_success', args=[order.order_number]))  # noqa
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "No items in the cart")
            return redirect(reverse('cart'))

        current_order = cart_contents(request)
        total_order = current_order['total']
        stripe_total = round(total_order * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserDetails.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except UserDetails.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')  # noqa

    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'cart_items': current_order['cart_items'],
        'total': current_order['total'],
    }

    return render(request, template, context)


def send_confirmation_email(order):
    """
    Sends a confirmation email to the user after placing an order.
    """

    subject = 'orders/confirmation_emails/confirmation_email_subject.txt'
    email_template_name = 'orders/confirmation_emails/confirmation_email_body.txt'  # noqa
    context = {'order': order}
    email_body = render_to_string(email_template_name, context)
    send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, [order.email])


def order_success(request, order_number):
    """
    View for handling successful orders.
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        # User is authenticated, proceed with accessing user details
        profile = UserDetails.objects.get(user=request.user)
        order.user_details = profile
        order.save()

        if save_info:
            user_data = {
                    'default_name': order.full_name,
                    'default_email': order.email,
                    'default_phone_number': order.phone_number,
                    'default_country': order.country,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
            }
            user_details_form = UserDetailsForm(user_data, instance=profile)
            if user_details_form.is_valid():
                user_details_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'orders/order_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


def remove_from_order(request, item_id):
    """
    View for removing an item from the order.
    """

    item = get_object_or_404(Item, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]
        messages.success(request, f'Removed {item.name} from your order')
        request.session['cart'] = cart
    else:
        messages.error(request, f'{item.name} is not in your cart')

    success_url = reverse("orders")
    return HttpResponseRedirect(success_url)
