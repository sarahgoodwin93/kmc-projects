
from django.contrib import admin
from .models import Contact, WhoWeAre


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


@admin.register(WhoWeAre)
class WhoWeAreAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not WhoWeAre.objects.exists()


admin.site.register(Contact, ContactAdmin)
