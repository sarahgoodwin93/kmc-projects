from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

"""
This code was taken from the walkthrough project Boutiuqe Ado >
The Checkout App > Admin, Signals & Forms Part 2.
Additional code comments have been added to show understanding.
"""


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal handler called after an OrderLineItem is saved.
    Updates the total price of the associated Order when a
    new OrderLineItem is created or an existing one is updated.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Signal handler called after an OrderLineItem is deleted.
    Updates the total price of the associated Order when an
    OrderLineItem is deleted.
    """
    instance.order.update_total()
