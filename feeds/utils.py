from feeds.reader import FeedReader
from feeds.models import FeedSource


def feed_refresh():
    """ Util that refreshes news feeds for all the sources. """
    sources = FeedSource.objects.all()
    list(map(lambda x: FeedReader(x.feed_url).posts(), sources))
