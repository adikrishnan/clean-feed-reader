import os
from datetime import timedelta
from django.conf import settings
from django.utils.timezone import now
from django.utils.log import logging
from feeds.reader import FeedReader
from feeds.models import FeedSource, FeedEntry

logger = logging.getLogger('feedreader')


def feed_refresh():
    """ Util that refreshes news feeds for all the sources. """
    sources = FeedSource.objects.all()
    list(map(lambda x: FeedReader(x.feed_url).posts(), sources))
    logger.info('Feed refresh complete')


def remove_old_entries():
    """ Util that removes old entries. """
    try:
        expire_days = int(os.getenv('FEED_EXPIRE_DAYS'))
    except ValueError:
        logger.info(
            f'Failed to set feed expiry,'
            f' defaulting to {settings.DEFAULT_FEED_EXPIRES_DAYS} days'
        )
        expire_days = settings.DEFAULT_FEED_EXPIRES_DAYS
    diff_date = now() - timedelta(days=expire_days)
    c, mc = FeedEntry.objects.filter(published__lte=diff_date).delete()
    logger.info(f'Total objects deleted: {c}')
    logger.info(f'Deleted objects per model: {mc}')
