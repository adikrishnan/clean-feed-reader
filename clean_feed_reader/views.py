from django.http import HttpResponse
from django.db.utils import IntegrityError
from feeds.reader import FeedReader
from feeds.models import FeedSource, FeedEntry


def load_objects(request):
    """ Load objects from source to DB """
    # Handle duplicates
    f = FeedSource.objects.all()
    source_posts = list(map(lambda x: FeedReader(x.feed_url).posts(), f))
    for source in source_posts:
        for item in source:
            try:
                FeedEntry.objects.create(**item)
            except IntegrityError:
                # Ignore errors for now
                pass
    return HttpResponse('Loaded objects')
