from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

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
    return render(request, "app_users/create_profile.html")
