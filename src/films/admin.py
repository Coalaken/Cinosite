from django.contrib import admin

from .models import Film, UserFilmRelation, FilmData


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(FilmData)
class FilmDataAdmin(admin.ModelAdmin):
    pass


@admin.register(UserFilmRelation)
class RelationsAdmin(admin.ModelAdmin):
    pass