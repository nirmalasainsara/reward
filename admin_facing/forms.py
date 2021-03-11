from django import forms

from .models import Application, Task


class AppForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            "category",
            "name",
            "points",
        )


class AppList(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["image"]


"""class AppDownloaded(forms.ModelForm):
    class Meta:
        model = App_list
        fields = (
            "Appname",
            "Points",
            "app_download",
        )
"""