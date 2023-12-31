from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Image


def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {'category': category, 'categories': categories, 'products': products}

    return render(request, 'products/products.html', context=context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'categories': categories,
    })


def about(request):
    categories = Category.objects.all()

    return render(request, 'products/menu/about.html', {
        'categories': categories
    })
