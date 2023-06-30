from django.contrib import admin
from .models import Product, Category, Image


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available', 'date_created', 'date_edited', 'category']
    list_editable = ['price', 'available']
    list_filter = ['price', 'available', 'date_created', 'date_edited', 'category']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ['img']