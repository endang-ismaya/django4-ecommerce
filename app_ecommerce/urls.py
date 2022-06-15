from django.urls import path
from . import views

app_name = "app_ecommerce"

urlpatterns = [
    path("", views.index),
    path("products/", views.products),
    path("products/<int:product_id>", views.product_detail, name="product_detail"),
]
