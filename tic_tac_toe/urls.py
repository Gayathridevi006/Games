# tic_tac_toe/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.tic_tac_toe_view, name="tic_tac_toe_view"),
]