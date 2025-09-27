from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("generate-matrix/", views.generate_matrix, name="generate_matrix"),
    path("find-paths/", views.find_paths, name="find_paths"),
]
from django.contrib import admin
