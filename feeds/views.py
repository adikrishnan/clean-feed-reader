from rest_framework.viewsets import ReadOnlyModelViewSet
from feeds.models import FeedSources, FeedSummary
from feeds.serializers import FeedSourcesSerializer, FeedSummarySerializer


class FeedSourcesViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedSources.objects.all()
    serializer_class = FeedSourcesSerializer


class FeedSummaryViewset(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = FeedSummary.objects.all()
    serializer_class = FeedSummarySerializer
