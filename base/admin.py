
from django.contrib import admin

from .models import Product
# Register your models here.


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ("name", "id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created",
        "number_doc",
        "created",
        "updated",
    )
    search_fields = (
        "name",
        "price",
        "number_doc",


    )
    list_filter = (

        "is_active",
        "created",
    )
