from rest_framework import serializers
from feeds.models import FeedSources, FeedSummary


class FeedSourcesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ['id', 'name', 'feed_url', 'last_refreshed']
        model = FeedSources
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }


class FeedSummarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = '__all__'
        model = FeedSummary
        extra_kwargs = {
            'url': {'lookup_field': 'id'},
        }
