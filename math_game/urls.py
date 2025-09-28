from django.urls import path
from . import views

urlpatterns = [
    path('', views.math_game_view, name='math_game'),
]
