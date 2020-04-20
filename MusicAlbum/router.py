from rest_framework.routers import DefaultRouter
from Album.views import MusicListView

router = DefaultRouter()
router.register('music_list', MusicListView, basename='api_music_album')
