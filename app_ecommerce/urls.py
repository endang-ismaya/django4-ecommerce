from django.urls import path
from . import views

app_name = "app_ecommerce"

urlpatterns = [
    path("", views.index),
    path("products/", views.ProductListView.as_view(), name="products"),
    path(
        "products/<int:pk>",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("products/add/", views.ProductCreateView.as_view(), name="add_product"),
    path(
        "products/update/<int:pk>",
        views.ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "products/delete/<int:product_id>", views.delete_product, name="delete_product"
    ),
    path("products/mylistings", views.my_listings, name="mylistings"),
]
