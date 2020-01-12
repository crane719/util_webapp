from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("convert/", views.MultiUploadView.as_view(), name="upload"),
]
