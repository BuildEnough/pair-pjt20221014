from django.shortcuts import render, redirect

from .forms import NewB, OldB
from django.contrib.auth import get_user_model, login as as_login, logout as as_logout

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):
    all_user = get_user_model().objects.all()
    context = {
        "all_user": all_user,
    }

    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = NewB(request.POST)
        if form.is_valid():
            form.save()
        return redirect("accounts:index")
    else:
        form = NewB()
        context = {"form": form}

    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            as_login(request, form.get_user())
        return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(reuqest):
    as_logout(reuqest)
    return redirect("accounts:index")


def detail(request, pk):
    user_inpo = get_user_model().objects.get(pk=pk)
    context = {
        "user_inpo": user_inpo,
    }

    return render(request, "accounts/detail.html", context)


def update(request):

    if request.method == "POST":
        form = OldB(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect("accounts:detail", request.user.pk)
    else:
        form = OldB(instance=request.user)
        context = {"change_form": form}

    return render(request, "accounts/update.html", context)
