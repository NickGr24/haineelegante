from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand

def index(request):
    categories = Category.objects.all()
    brands = Brand.objects.all().order_by("name")
    
    # Создаем список уникальных первых букв брендов
    first_letters = sorted(set(brand.name[0].upper() for brand in brands if brand.name))

    products = Product.objects.all()
    
    return render(request, "products/index.html", {
        "categories": categories,
        "brands": brands,
        "products": products,
        "first_letters": first_letters
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/product_detail.html", {"product": product})

def brand_products(request, brand_name):
    brand = get_object_or_404(Brand, name=brand_name)
    products = Product.objects.filter(brand=brand)
    return render(request, "products/brand_products.html", {"brand": brand, "products": products})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_products.html', {'category': category, 'products': products})