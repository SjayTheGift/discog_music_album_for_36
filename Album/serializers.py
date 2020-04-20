from rest_framework import serializers
from .models import Music


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api_music_album-detail',
        lookup_field='pk')

    class Meta:
        model = Music
        fields = ['url', 'cover_image', 'artist', 'title', 'label', 'year', 'catalogue_number']
