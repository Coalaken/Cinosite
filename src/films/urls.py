from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('add/film/', views.FilmCreateView.as_view(), name='add'),
    path('bookmarks/', views.bookmarks, name="bookmarks"),
    path('films/<int:pk>/', views.film_page, name="film_page"),
    path('films/by-category/<int:pk>/', views.by_category, name="by_category"),
    ###
    path('films/stream/<int:pk>/', views.get_streaming_video, name="stream")
]
