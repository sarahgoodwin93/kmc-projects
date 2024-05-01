from django.contrib import admin
from . models import Item, Type


# Admin adjustments for Items.
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'type',
        'price',
        'manufactured_by',
        'item_number',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Type)
