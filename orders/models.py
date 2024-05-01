import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from items.models import Item
from users.models import UserDetails

"""
The base of this code was taken and modified from the walkthrough
project Boutiuqe Ado > The Checkout App > Models Part 2.
Additional code comments have been added to show understanding.
Parts have been removed that were not relevant to this site and some
naming has been changed to better suit KMC Projects.
"""


class Order(models.Model):
    """
    The Order model has a unique identifier for each order with
    the order number, then asks for the customer details, adds the
    date and time when the order was created
    and has the total price of the order.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_details = models.ForeignKey(UserDetails, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='user_orders')  # noqa
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(max_length=56, blank_label='Country *', null=False, blank=False)  # noqa
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # noqa

    def _generate_order_number(self):
        """
        Generates a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total price each time a line item is added
        """
        self.total_price = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0  # noqa
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the order by its order number.
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    The OrderLineItem model finds the order to which this line item belongs,
    then the item being ordered, the quantity of the item in this line item,
    and the total price for this line item.
    """
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')  # noqa
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)  # noqa
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)  # noqa

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total. This then calculates the total
        price for this line item
        """
        self.lineitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the line item
        showing the SKU and order number.
        """
        return f'SKU {self.item.sku} on order {self.order.order_number}'
