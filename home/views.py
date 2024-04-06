from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def kmc_home(request):
    return HttpResponse("Hello, World!")