from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("products", views.products),
    path("products/<int:product_id>", views.product_detail),
]
