from django.shortcuts import render

# Create your views here.
def OrderView(request):
    cart = request.session.get('bag', {})
    if not cart:
        messages.error(request, "No items in the cart")
        return redirect(reverse('items'))
    
