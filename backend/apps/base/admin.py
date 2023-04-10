from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "file1",
        "title",
        "is_active",
        "created",
        "number_doc",
        "created",
        "updated",
    )
    search_fields = (
        "title",
        "number_doc",


    )
    list_filter = (

        "is_active",
        "created",
    )

    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.file1.url}" style="max-height: 330px;">')