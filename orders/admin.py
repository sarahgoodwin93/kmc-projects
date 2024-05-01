from django.contrib import admin
from .models import Order, OrderLineItem

# Admin adjustments for OrderLineItemAdminInline
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

# Admin adjustments for Order Model.
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',)

    fields = ('order_number', 'user_details', 'full_name', 'email', 'phone_number',
    'country', 'postcode', 'town_or_city', 'street_address1',
    'street_address2', 'date', 'total_price',)

    list_display = ('order_number', 'date', 'full_name', 'total_price')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
