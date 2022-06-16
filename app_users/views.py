from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.
def register(request):
    form = NewUserForm()
    context = {"form": form}

    return render(
        request=request, template_name="app_users/register.html", context=context
    )
