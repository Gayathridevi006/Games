"""
URL configuration for matrix_game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from game import views as game_views  # import views if needed


def home_view(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),  # Homepage
    path("game/", include("game.urls")),            # Other game app
    path("generate-matrix/", game_views.generate_matrix, name="generate_matrix"),
    path("find-paths/", game_views.find_paths, name="find_paths"),
    path("tic_tac_toe/", include("tic_tac_toe.urls")),  # Tic-Tac-Toe app
    path('math-game/', include('math_game.urls')),
]