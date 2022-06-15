from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "app_ecommerce/index.html", context=context)


def product_detail(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        context = {"product": product}
        return render(
            request=request, template_name="app_ecommerce/detail.html", context=context
        )
    except:
        return HttpResponse("Product not found.")
