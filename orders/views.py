from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import OrderForm
from items.models import Item

# Create your views here.
def OrderView(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "No items in the cart")
        return redirect(reverse('cart'))
    
    order_form = OrderForm()
    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
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
    
