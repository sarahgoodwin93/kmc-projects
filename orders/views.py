from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from items.models import Item
from users.forms import UserDetailsForm
from users.models import UserDetails
from cart.context import cart_contents

import stripe

# Create your views here.
# Order and stripe view
def OrderView(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
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
                    messages.error(request, "One of the items in your cart wasn't found in our database. Please reach out for assistance!")
                    order.delete()
                    return redirect(reverse('cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_success', args=[order.order_number]))
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

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')
    
    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'cart_items': current_order['cart_items'],
        'total': current_order['total'],
    }

    return render(request, template, context)

# Order Success

def order_success(request, order_number):
    """
    Handle successful orders
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    profile = UserDetails.objects.get(user=request.user)
    order.user_details = profile
    order.save()

    if save_info:
        user_data = {
                'default_email' : order.email,
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


# Remove from Order View

def remove_from_order(request, item_id):
    """ Remove item from order """

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
    
