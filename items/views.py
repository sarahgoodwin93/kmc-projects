from django.shortcuts import render
from .models import Item

# Create your views here.

def items(request):
    """ A view to return the items page """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'items/items.html', context)