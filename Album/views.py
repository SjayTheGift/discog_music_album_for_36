from rest_framework import filters
from rest_framework import viewsets, permissions

from .serializers import MusicSerializer
from .models import Music


class MusicListView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist', 'title', 'label', 'year', 'catalogue_number']
    ordering_fields = ['artist', 'title', 'label', 'year', 'catalogue_number']
    permission_classes = [permissions.IsAuthenticated]
