from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'body',
        'created_on',
        'active',
    )


admin.site.register(Review, ReviewAdmin)