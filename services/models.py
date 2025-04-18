from django.db import models
from ckeditor.fields import RichTextField


# Services Model
class Services(models.Model):
    """
    The Services Model stores information about the services, including
    its title, description and timestamps.
    """
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    description = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Case Study Model
class CaseStudy(models.Model):
    """
    The CaseStudy Model stores information about the case studies, including
    their title, body, image and timestamps.
    """
    title = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, unique=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    def __str__(self):
        return self.title
