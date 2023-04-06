from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
