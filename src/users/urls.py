from django.urls import path

from . import views


urlpatterns = [
    path('sign-up/', views.RegistrationUser.as_view(), name='sign_up'),
    path('users/<int:pk>/profile/', views.profile_page, name='profile'),
]
