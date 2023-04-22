from rest_framework.viewsets import ModelViewSet
from django.db.models import When, Case, Count


from ..models import Film
from .serializer import FilmSerializer
from .permissions import IsOwnerOrStaffOrReadOnly


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all().annotate(
        annotated_likes=(
            Count(Case(When(userfilmrelation__like=True, then=1)))
        )
    )
    serializer_class = FilmSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly, ]
    
    def perform_create(self, serializer):
        serializer.validated_data["added_by"] = self.request.user
        serializer.save()