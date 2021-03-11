from django.contrib import admin
from django.urls import path
from . import views

app = "user_facing"

urlpatterns = [
    # path("", views.index, name="home"),
    path("user_facing/login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile")
    # path("userfacing/profile/", views.profile_view, name="profile_view"),
]