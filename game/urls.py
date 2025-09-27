from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.game, name="game_view"),
    path("generate-matrix/", views.generate_matrix, name="generate_matrix"),
    path("find-paths/", views.find_paths, name="find_paths"),
]