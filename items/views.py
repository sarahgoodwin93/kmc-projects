from django.shortcuts import render

# Create your views here.

def items(request):
    """ A view to return the items page """

    return render(request, 'items/items.html')