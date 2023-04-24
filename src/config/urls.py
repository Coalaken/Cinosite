from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import urls as users_urls
from films.films_api import urls as films_api_urls

urlpatterns = [
    path('SoGood/', include('films.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += users_urls.urlpatterns
urlpatterns += films_api_urls.urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)