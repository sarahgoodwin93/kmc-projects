from django.contrib import admin
from . models import Item, Type

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'type',
        'price',
        'preferred_supplier',
        'item_number',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Type)
