import os
from datetime import timedelta
from django.utils.timezone import now
from django.utils.log import logging
from feeds.reader import FeedReader
from feeds.models import FeedSource, FeedEntry

logger = logging.getLogger('feedreader')


def feed_refresh():
    """ Util that refreshes news feeds for all the sources. """
    sources = FeedSource.objects.all()
    list(map(lambda x: FeedReader(x.feed_url).posts(), sources))
    logger.info(f'Feed refresh complete')


def remove_old_entries():
    """ Util that removes old entries. """
    expire_days = os.getenv('FEED_EXPIRE_DAYS', 2)
    diff_date = now() - timedelta(days=expire_days)
    count, model_count = FeedEntry.objects.filter(published__lte=diff_date).delete()
    logger.info(f'Total objects deleted: {count}')
    logger.info(f'Deleted objects per model: {model_count}')
