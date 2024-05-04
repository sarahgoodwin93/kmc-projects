from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from items.models import Item


# Create your views here.
def cart_view(request):
    """ 
    Return cart page with items added to the cart
    Or show No items in cart if none have been added
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add or update the quantity of the specified item in the shopping cart
    """

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # Item is already in the cart, update the quantity
        cart[item_id] += quantity
        messages.success(request, f'Updated {item.name} quantity in your cart')
    else:
        # Item is not in the cart, add it
        cart[item_id] = quantity
        messages.success(request, f'Added {item.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ 
    Remove item from cart and give success message
    """

    item = get_object_or_404(Item, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]
        messages.success(request, f'Removed {item.name} from your cart')
        request.session['cart'] = cart
    else:
        messages.error(request, f'{item.name} is not in your cart')

    success_url = reverse("cart")
    return HttpResponseRedirect(success_url)
