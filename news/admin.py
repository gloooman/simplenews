from django.contrib import admin
from .models import News
from tinymce.widgets import TinyMCE
from django.db import models


@admin.register(News)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'article', 'status', 'author']
    exclude = ['author']
    list_filter = ['author', 'status']

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            if not obj.author.premoderation:
                obj.status = 'APR'
        super().save_model(request, obj, form, change)
