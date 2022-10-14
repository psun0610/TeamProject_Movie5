from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as mylogin
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


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            mylogin(request, form.get_user())
            return
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)