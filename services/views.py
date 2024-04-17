from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Services, CaseStudy

# Create your views here.

def ServiceList(request):
    services = Services.objects.all()
    return render(request, 'services/services.html', {'services': services})
