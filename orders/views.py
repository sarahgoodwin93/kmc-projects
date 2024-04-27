from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import OrderForm
from items.models import Item
from cart.context import cart_contents
from django.conf import settings
import stripe

# Create your views here.
def OrderView(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

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
    
