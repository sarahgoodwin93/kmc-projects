from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Contact Model for business.
class Contact(models.Model):
    """
    Contact form to use for site users to contact KMC Projects
    A dropdown list of the services offered to help direct their
    enquiry.
    """
    CONSULTING = 'Consulting'
    PROJECT_MANAGEMENT = 'Project Management'
    TRAINING = 'Training'
    DESIGN = 'Design'
    OTHER = 'Other'

    SERVICE_CHOICES = [
        (CONSULTING, 'Consulting'),
        (PROJECT_MANAGEMENT, 'Project Management'),
        (TRAINING, 'Training'),
        (DESIGN, 'Design'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # noqa
    email = models.EmailField(unique=True)
    service_needed = models.CharField(max_length=100, choices=SERVICE_CHOICES, null=True, blank=True)  # noqa
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Who we are Model
class WhoWeAre(models.Model):
    """
    The who we are Model stores information for the homepage text, including
    its title, description and timestamps.
    """
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    description = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    def __str__(self):
        return self.name
