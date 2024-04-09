from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item

# Create your views here.

def items(request):
    """ A view to return the items page and be able to search for items """

    items = Item.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No items found")
                return redirect(reverse('items'))
            
            queries = Q(name__icontains=query) | Q(item_number__icontains=query)
            items = items.filter(queries)

    context = {
        'items': items,
    }

    return render(request, 'items/items.html', context)