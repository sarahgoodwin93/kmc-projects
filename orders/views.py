from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def OrderView(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "No items in the cart")
        return redirect(reverse('items'))
    
    order_form = OrderForm()
    template = 'orders/orders.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
    
