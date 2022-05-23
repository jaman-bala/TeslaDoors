
from django.contrib import admin

from .models import Product, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "is_active",
        "created",
        "number_doc",
    )
    search_fields = (
        "name",
        "price",
        "number_doc",
        "category__name",

    )
    list_filter = (
        "category__name",
        "is_active",
        "created",
    )
