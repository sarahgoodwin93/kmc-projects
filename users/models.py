from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

"""
The base of this code was taken and modified from the walkthrough 
project Boutiuqe Ado > The Checkout App > Profile App - Part 2.
Additional code comments have been added to show understanding.
Parts have been removed that were not relevant to this site and some
naming has been changed to better suit KMC Projects.  
"""

class UserDetails(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=False, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(max_length=56, blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_details(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserDetails.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userdetails.save()