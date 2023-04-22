from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Film, UserFilmRelation


class FilmSerializer(serializers.ModelSerializer):
    annotated_likes = serializers.IntegerField(read_only=True)
    class Meta:
        model = Film
        fields = ('name', 'description',
                  'author', 'image',
                  'video',
                  'created_at', 'annotated_likes')