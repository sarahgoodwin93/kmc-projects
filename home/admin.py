from django.contrib import admin
from .models import Contact, NewsletterSignUp

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'email',
        'message',
        'created_on',
    )

    ordering = ('created_on',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsletterSignUp)
