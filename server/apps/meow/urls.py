from django.urls import path

from apps.meow.views import start_task

urlpatterns = [
    path("", start_task, name="run_task"),
]
