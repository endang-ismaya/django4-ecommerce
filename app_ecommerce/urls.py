from django.urls import path
from . import views

app_name = "app_ecommerce"

urlpatterns = [
    path("", views.index),
    path("products/", views.products, name="product"),
    path("products/<int:product_id>", views.product_detail, name="product_detail"),
    path("products/add/", views.add_product, name="add_product"),
    path(
        "products/update/<int:product_id>", views.update_product, name="update_product"
    ),
    path(
        "products/delete/<int:product_id>", views.delete_product, name="delete_product"
    ),
]
