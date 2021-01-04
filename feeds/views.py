from rest_framework.viewsets import ReadOnlyModelViewSet
from feeds.models import FeedSource, FeedEntry
from feeds.serializers import FeedSourceSerializer, FeedSerializer


class FeedSourceViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedSource.objects.all()
    serializer_class = FeedSourceSerializer


class FeedViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedEntry.objects.all()
    serializer_class = FeedSerializer
