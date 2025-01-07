from django.urls import path

from videotape import views

urlpatterns = [
    path("", views.index, name="index"),
]