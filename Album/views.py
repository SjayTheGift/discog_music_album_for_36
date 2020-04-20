from rest_framework import viewsets, permissions

from .serializers import MusicSerializer
from .models import Music


class MusicListView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated]