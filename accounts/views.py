from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .forms import Myform

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
            return
    else:
        form = Myform()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
