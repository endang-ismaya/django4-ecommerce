from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


# def products(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "app_ecommerce/index.html", context=context)


class ProductListView(ListView):
    model = Product
    template_name: str = "app_ecommerce/index.html"
    context_object_name: list[str] = "products"


# def product_detail(request, product_id):

#     try:
#         product = Product.objects.get(id=product_id)
#         context = {"product": product}
#         return render(
#             request=request, template_name="app_ecommerce/detail.html", context=context
#         )
#     except:
#         return HttpResponse("Product not found.")


class ProductDetailView(DetailView):
    model = Product
    template_name: str = "app_ecommerce/detail.html"
    context_object_name: dict[str] = "product"


@login_required
def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES["upload"]
        seller_name = request.user

        product: Product = Product(
            name=name, price=price, desc=desc, image=image, seller_name=seller_name
        )

        product.save()

    return render(request, "app_ecommerce/add_product.html")


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "price", "desc", "image", "seller_name"]


@login_required
def update_product(request, product_id):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES.get("upload", None)

        product: Product = Product.objects.get(id=product_id)
        product.name = name
        product.price = price
        product.desc = desc

        if image is not None:
            print(image)
            product.image = image

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


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "price", "desc", "image", "seller_name"]
    template_name_suffix: str = "_update_form"


@login_required
def delete_product(request, product_id):
    # print(f"product_id: {product_id}")
    try:
        product = Product.objects.get(id=product_id)

        if request.method == "POST":
            product.delete()
            return redirect("/products/")

        else:
            context = {"product": product}
            print(product)
            return render(
                request,
                "app_ecommerce/delete_product.html",
                context,
            )

    except:
        return HttpResponse(f"Product not found for id={product_id}")


@login_required
def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {"products": products}
    return render(request, "app_ecommerce/mylistings.html", context)
