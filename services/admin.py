from django.contrib import admin
from . models import Services, CaseStudy

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
    )

    ordering = ('sku',)

class CaseStudyAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'body',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Services, ServicesAdmin)
admin.site.register(CaseStudy, CaseStudyAdmin)