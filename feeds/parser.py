import time
import uuid
import hashlib
from pytz import timezone
from datetime import datetime
import requests
import feedparser
from django.utils.timezone import now
from bs4 import BeautifulSoup
from .models import FeedEntry, FeedSource


# TODO: Use a different pattern that separates individual record transformation
# from transformation of set of records.
class ParserFactory:
    """ An abstract factory implementation to handle specific feed parsers
    as required. """
    extract_fields = {
        'title': 'title',
        'author': 'author',
        'link': 'link',
        'summary': 'summary',
        'published': 'published_parsed',
        'updated': 'updated_parsed',
    }

    def __init__(self, feed_url, full_article=False):
        self.feed_url = feed_url
        self.full_article = full_article
        self._entries = None

    @property
    def parser(self):
        """ A feedparser parser. """
        if not self.feed_url:
            raise RuntimeError('Feed URL cannot be empty')
        return feedparser.parse(self.feed_url)

    @property
    def entries(self):
        """ All entries as provided by parser """
        return self._build_entries()

    @property
    def article_reference(self):
        """ {type: name} dict to be used for identifying post details and
        extracting. """
        raise NotImplementedError(
            'This property needs to be implemented for all sources'
        )

    def _get_article(self, link):
        """ Get full post detail for a specific feed entry. """
        try:
            r = requests.get(link)
            page = r.text
            soup = BeautifulSoup(page, 'lxml')
            post = soup.find(**self.article_reference).text
            return post
        except Exception as ex:
            return 'Encountered errors while extracting full post'

    def _transform(self, data_dict):
        """ Transform the dictionary to include fields as per model. """
        model_data = {
            key: data_dict.get(value)
            for key, value in self.extract_fields.items()
        }
        model_data['id'] = uuid.UUID(
            hashlib.md5(model_data.get('title').encode('utf-8')).hexdigest()
        )
        model_data['source'] = model_data.get('link').split('/')[2]
        if not model_data.get('author'):
            model_data['author'] = model_data['source']
        model_data['published'] = datetime.fromtimestamp(
            time.mktime(model_data.get('published')), tz=timezone('Asia/Kolkata')
        )
        model_data['updated'] = datetime.fromtimestamp(
            time.mktime(model_data.get('updated')), timezone('Asia/Kolkata')
        )
        model_data['summary'] = BeautifulSoup(
            model_data.get('summary'), "lxml"
        ).text
        if self.full_article:
            model_data['article'] = self._get_article(model_data.get('link'))
        return model_data

    def save_feed_entries(self):
        """ Save the entries to the database. """
        feed_entries = map(lambda x: FeedEntry(**x), self._entries)
        FeedEntry.objects.bulk_create(feed_entries, ignore_conflicts=True)
        source = FeedSource.objects.get(feed_url=self.feed_url)
        source.last_refreshed = now()
        source.save()

    def _build_entries(self):
        """ Manually build full post entries using each link the feed. """
        if not self._entries:
            self._entries = self.parser.get('entries')
        self._entries = list(map(self._transform, self._entries))
        self.save_feed_entries()
        return self._entries


class GenericParser(ParserFactory):
    """ Default Parser implementation. """
    pass


class ScrollParser(ParserFactory):
    """ Parser implementation for Scroll source. """

    @property
    def article_reference(self):
        return {'id': 'article-contents'}


class NewsMinuteParser(ParserFactory):
    """ Parser implementation for NewsMinute source. """

    @property
    def article_reference(self):
        return {'class_': 'article-content'}


class MoneyControlParser(ParserFactory):
    """ Parser implementation for NewsMinute source. """

    @property
    def article_reference(self):
        return {'class_': 'arti-flow'}
