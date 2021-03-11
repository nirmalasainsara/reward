from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Application(models.Model):
    Socialmedia = "Socialmedia"
    Heatlhmanagement = "HealthManagement"
    Entertainment = "Entertainment"
    Educational = "Educational"
    Productivity = "Productivity"
    Lifestyle = "Lifestyle"
    FIELD_IN_CATEGORY_CHOICES = [
        (Socialmedia, "Socialmedia"),
        (Heatlhmanagement, "Heatlhmanagement"),
        (Entertainment, "Entertainment"),
        (Educational, " Educational"),
        (Productivity, "Productivity"),
        (Lifestyle, "Lifestyle"),
    ]
    category = models.CharField(
        max_length=200,
        choices=FIELD_IN_CATEGORY_CHOICES,
        default=Socialmedia,
    )

    name = models.CharField(max_length=200)
    points = models.IntegerField()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    image = models.ImageField()
