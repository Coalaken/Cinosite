from rest_framework.viewsets import ModelViewSet
from django.db.models import When, Case, Count
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
        
        
# @csrf_exempt
# @permission_required((IsAuthenticatedOrReadOnly, ))        
# @login_required(login_url=reverse_lazy('home'))
# @api_view(["GET", "POST"])
# def film_list(request):
#     if request.method == "GET":
#         try:
#             films = Film.objects.all()
#         except Exception as e:
#             return Response({
#                 'data': {},
#                 'message': f'Some error {e}' 
#             }, status=status.HTTP_400_BAD_REQUEST)
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         try:
#             data = request.data
#             serializer = FilmSerializer(data, many=True)
#             if serializer.is_valid():
#                 serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({
#                 'data': {},
#                 'message': f'Some error {e}' 
#             }, status=status.HTTP_400_BAD_REQUEST)
        
    