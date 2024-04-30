from django.shortcuts import render, get_object_or_404, redirect, reverse

# Handle 404 View
def handle404(request, exception):
    """
    404 error page.
    """
    return render(request, "404.html", status=404)

# Handle 404 View
def handle403(request, exception):
    """
    403 error page.
    """
    return render(request, "403.html", status=403)


# Handle 500 View
def handle500(request):
    """
    500 error page.
    """
    return render(request, "500.html", status=500)