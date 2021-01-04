from rest_framework import serializers
from feeds.models import FeedSources, FeedEntry


class FeedSourcesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ['id', 'name', 'feed_url', 'last_refreshed']
        model = FeedSources
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }


class FeedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = '__all__'
        model = FeedEntry
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }
