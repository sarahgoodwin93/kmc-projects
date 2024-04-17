from django.shortcuts import render, redirect
from django.contrib import messages

from items.models import Item

# Create your views here.

def cart_view(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified item to the shopping cart """

    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {item.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)