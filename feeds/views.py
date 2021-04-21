from rest_framework.viewsets import ReadOnlyModelViewSet
from feeds.models import FeedSource, FeedEntry
from feeds.serializers import FeedSourceSerializer, FeedSerializer
from django_filters import rest_framework as filters


class FeedSourceViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedSource.objects.all()
    serializer_class = FeedSourceSerializer


class FeedViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedEntry.objects.all()
    serializer_class = FeedSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('source',)
