from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "app_users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="app_users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="app_users/logout.html"),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
    path("create-profile/", views.create_profile, name="create_profile"),
    path("seller-profile/<int:user_id>/", views.seller_profile, name="seller_profile"),
]
