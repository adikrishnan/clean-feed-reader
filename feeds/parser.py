import time
import uuid
import hashlib
from datetime import datetime
from abc import ABC, abstractmethod
import requests
import feedparser
from bs4 import BeautifulSoup
from .models import FeedSummary


# TODO: Use a different pattern that separates individual record transformation
# from transformation of set of records.
class ParserFactory(ABC):
    """ An abstract factory implementation to handle specific feed parsers
    as required. """
    MIN_WORDS = 30
    EXTRACT_FIELDS = {
        'title': 'title',
        'author': 'author',
        'link': 'link',
        'summary': 'summary',
        'published': 'published_parsed',
        'updated': 'updated_parsed',
        # 'summary': 'post', TODO: Enable this later
    }

    def __init__(self, feed_url, full_post=False):
        self.feed_url = feed_url
        self.full_post = full_post
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

    @abstractmethod
    def filter_text(self, text):
        """ Filter to weed out any text that might not be related to the
        post itself.
        """
        # TODO: Fix logic before enabling full post retrieval
        if len(text.split(' ')) > self.MIN_WORDS:
            return text

    def _get_post(self, link):
        """ Get full post detail for a specific feed entry. """
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        post = list(
            filter(
                None,
                map(self.filter_text, soup.stripped_strings)
            )
        )
        return '\n'.join(post)

    def _transform(self, data_dict):
        """ Transform the dictionary to include fields as per model. """
        model_data = {key: data_dict.get(value) for key, value in self.EXTRACT_FIELDS.items()}
        model_data['id'] = uuid.UUID(
            hashlib.md5(model_data.get('title').encode('utf-8')).hexdigest()
        )
        model_data['source'] = model_data.get('link').split('/')[2]
        if not model_data.get('author'):
            model_data['author'] = model_data['source']
        model_data['published'] = datetime.fromtimestamp(
            time.mktime(model_data.get('published'))
        )
        model_data['updated'] = datetime.fromtimestamp(
            time.mktime(model_data.get('updated'))
        )
        if self.full_post:
            model_data['post'] = self._get_post(model_data.get('link'))
        return model_data

    def save_posts(self):
        """ Save the entries to the database. """
        feed_entries = map(lambda x: FeedSummary(**x), self._entries)
        FeedSummary.objects.bulk_create(feed_entries, ignore_conflicts=True)

    def _build_entries(self):
        """ Manually build full post entries using each link the feed. """
        if not self._entries:
            self._entries = self.parser.get('entries')
        self._entries = list(map(self._transform, self._entries))
        self.save_posts()
        return self._entries


class GenericParser(ParserFactory):
    """ Generic parser implementation. """

    def filter_text(self, text):
        """ Override abstract implementation """
        return super().filter_text(text)
