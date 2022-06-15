from django.http import HttpResponse
from django.shortcuts import render, redirect
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


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES["upload"]

        product: Product = Product(name=name, price=price, desc=desc, image=image)

        product.save()

    return render(request, "app_ecommerce/add_product.html")


def update_product(request, product_id):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES["upload"]

        product: Product = Product(name=name, price=price, desc=desc, image=image)

        product.save()

        return redirect("/products/")
    else:
        try:
            product = Product.objects.get(id=product_id)
            context = {"product": product}
            return render(
                request=request,
                template_name="app_ecommerce/update_product.html",
                context=context,
            )
        except:
            return HttpResponse("Product not found.")


def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)

        if request.method == "POST":
            product.delete()
            return redirect("/products/")

        else:
            context = {"product": product}
            return render(
                request=request,
                template_name="app_ecommerce/delete_product.html",
                context=context,
            )
    except:
        return HttpResponse("Product not found.")
