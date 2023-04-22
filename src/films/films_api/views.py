from rest_framework.viewsets import ModelViewSet
from django.db.models import When, Case, Count

from ..models import Film
from .serializer import FilmSerializer


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all().annotate(
        annotated_likes=(
            Count(Case(When(userfilmrelation__like=True, then=1)))
        )
    )
    serializer_class = FilmSerializer