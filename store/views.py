from django.shortcuts import render,get_object_or_404

from .models import Category,Product

# Create your views here.

def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    for product in products:
        for image in product.product_image.all():
            print(image.is_feature)
    return render(request, "store/index.html", {"products": products})

def category_list(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "store/category.html", {"category": category, "products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})