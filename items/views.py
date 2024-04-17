from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item, Type

# Create your views here.

def items(request):
    """ A view to return the items page and be able to search for items """

    items = Item.objects.all()
    query = None
    type = None

    if request.GET:
        if 'type' in request.GET:
            type = request.GET['type'].split(',')
            items = items.filter(type__name__in=type)
            type = Type.objects.filter(name__in=type)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No items found, please enter the name or item number")
                return redirect(reverse('items'))
            
            queries = Q(name__icontains=query) | Q(item_number__icontains=query)
            items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
        'current_type': type,
    }

    return render(request, 'items/items.html', context)