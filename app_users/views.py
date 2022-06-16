from django.shortcuts import redirect, render
from .forms import NewUserForm

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
