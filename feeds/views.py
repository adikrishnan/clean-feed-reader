from rest_framework.viewsets import ReadOnlyModelViewSet
from feeds.models import FeedSources, FeedEntry
from feeds.serializers import FeedSourcesSerializer, FeedSerializer


class FeedSourcesViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedSources.objects.all()
    serializer_class = FeedSourcesSerializer


class FeedViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedEntry.objects.all()
    serializer_class = FeedSerializer
