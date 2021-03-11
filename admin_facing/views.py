from django.shortcuts import render, redirect, reverse
from .models import Application, Task
from .forms import AppForm, AppList
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@staff_member_required
def app_view(request):
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AppForm()
    context = {"form": form}
    return render(request, "admin_facing/app.html", context)


@login_required
def task_create(request, app_id):
    app = Application.objects.get(id=app_id)
    if request.method == "POST":
        # app_id = request.kwargs.get("app_id")
        form = AppList(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data["image"]
            fs = FileSystemStorage()
            image = fs.save(img.name, img)
            qs = Task.objects.filter(user=request.user, application=app)
            if qs.exists():
                messages.warning(request, "user already exists.")
                return redirect(reverse("admin_facing:home"))
            task = Task.objects.create(user=request.user, application=app, image=image)
            return redirect(reverse("admin_facing:task_claimed"))
    else:
        form = AppList()
    context = {"form": form, "app": app}
    return render(request, "admin_facing/app_list.html", context)


def user_home_view(request):
    app = Application.objects.all()
    context = {"app": app}
    return render(request, "admin_facing/task_create.html", context)


@login_required
def task_claimed(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    points = 0
    for task in tasks:
        points += task.application.points
    context = {"points": points, "tasks": tasks}
    return render(request, "admin_facing/task_claimed.html", context)


@login_required
def user_claimed_task_list(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    context = {"tasks": tasks}
    return render(request, "admin_facing/task_claimed_list.html", context)