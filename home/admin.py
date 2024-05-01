from django.contrib import admin
from .models import Contact

# Admin adjustments for Contact Form.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'email',
        'service_needed',
        'message',
        'created_on',
    )

    ordering = ('created_on',)

admin.site.register(Contact, ContactAdmin)
