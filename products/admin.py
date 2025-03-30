from django.contrib import admin
from .models import Product, Category, Brand, ProductImage, SliderImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Количество пустых форм для добавления

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price', 'discount', 'created_at')
    list_filter = ('category', 'brand')
    search_fields = ('title', 'brand__name', 'category__name')
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active', 'order']
    list_editable = ['active', 'order']
