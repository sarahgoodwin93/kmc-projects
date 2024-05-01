from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        added_item = get_object_or_404(Item, pk=item_id)
        item_total_cost = quantity * added_item.price
        total += item_total_cost
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'added_item': added_item,
            'item_total_cost': item_total_cost
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context
