from django.contrib import admin
from . models import Services, CaseStudy


# Admin adjustments for Services List.
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
    )

    ordering = ('sku',)


# Admin adjustments for Case study List.
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
