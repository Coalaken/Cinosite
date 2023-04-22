from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('api/v1/films', views.FilmViewSet, basename='api_films')

urlpatterns = [
    path('', include('rest_framework.urls'))
]

urlpatterns += router.urls