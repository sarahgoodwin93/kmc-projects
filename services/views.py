from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Services, CaseStudy

# Create your views here.

def ServicesView(request):
    """ A view to return the services page """

    services = Services.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No services found")
                return redirect(reverse('services'))
            
            queries = Q(name__icontains=query) | Q(services_number__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def CaseStudyView(request):
    """ A view to return the casestudies section """

    casestudy = CaseStudy.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No case studies found")
                return redirect(reverse('casestudy'))
            
            queries = Q(name__icontains=query) | Q(casestudy_number__icontains=query)
            casestudy = casestudy.filter(queries)

    context = {
        'casestudy': casestudy,
    }

    return render(request, 'casestudy/services.html', context)