from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    path('SoGood/', views.home)
]
