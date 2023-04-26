from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('api/v1/films', views.FilmViewSet, basename='api_films')

urlpatterns = [
    path('', include('rest_framework.urls')),
    # path('api/v2/films', views.film_list, name="films-lisst")
]

urlpatterns += router.urls