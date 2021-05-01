from rest_framework import serializers
from feeds.models import FeedSource, FeedEntry


class FeedSourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ['id', 'name', 'feed_url', 'last_refreshed']
        model = FeedSource
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    source = serializers.CharField(source='source.name')

    class Meta:
        fields = '__all__'
        model = FeedEntry
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }
