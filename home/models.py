from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Contact Model for business.
class Contact(models.Model):
    """
    Contact form to use for site users to contact the admin
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    service_needed = models.CharField(max_length=100, choices=SERVICE_CHOICES, null=True, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


