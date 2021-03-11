from django.contrib import admin
from django.urls import path
from . import views

app_name = "admin_facing"

urlpatterns = [
    path("home/", views.user_home_view, name="home"),
    path("category/", views.app_view, name="app"),
    path("task_create/<int:app_id>/", views.task_create, name="task_create"),
    path("task_claimed/", views.task_claimed, name="task_claimed"),
    path("task_claimed_list/", views.user_claimed_task_list, name="task_claimed_list")
    # path("appdownloaded/", views.userdownloadapp, name="appdownloaded"),
]