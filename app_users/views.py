from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)

            return redirect("/products/")

    form = NewUserForm()
    context = {"form": form}

    return render(
        request=request, template_name="app_users/register.html", context=context
    )


@login_required
def profile(request):
    return render(request, "app_users/profile.html")


def create_profile(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        image = request.FILES["upload"]
        user = request.user

        profile = Profile(user=user, contact=contact, image=image)
        profile.save()

    return render(request, "app_users/create_profile.html")


def seller_profile(request, user_id):
    seller = User.objects.get(id=user_id)
    context = {"seller": seller}
    return render(request, "app_users/seller_profile.html", context)
