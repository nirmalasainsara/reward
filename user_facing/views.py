from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.urls import reverse
from django.template.context_processors import csrf

User = get_user_model()


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse("admin_facing:home"))
    return render(request, "user_facing/form.html", {"form": form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")

    context = {"form": form}
    return render(request, "user_facing/form.html", context)


def logout_view(request):
    logout(request)
    return redirect(reverse("user_facing:login"))


def profile_view(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "user_facing/user_profile.html", context)