from abc import ABC, abstractmethod
import requests
import feedparser
from bs4 import BeautifulSoup


class ParserFactory(ABC):
    """ An abstract factory implementation to handle specific feed parsers
    as required. """
    MIN_WORDS = 30

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
        if not self._entries:
            self._entries = self.parser.get('entries')
        # Entries are excerpts only and full post needs to be retrieved from
        # the feed after sufficient post transformation.
        if self.full_post:
            return self._build_entries()
        return self._entries

    @abstractmethod
    def filter_text(self, text):
        """ Filter to weed out any text that might not be related to the
        post itself.
        """
        # A basic logic based on number of words in the post.
        if len(text.split(' ')) > self.MIN_WORDS:
            return text

    def _build_entries(self):
        """ Manually build full post entries using each link the feed. """
        if not self._entries:
            self._entries = self.parser.get('entries')
        for item in self._entries:
            if not item.get('post'):
                r = requests.get(item['link'])
                soup = BeautifulSoup(r.text, 'html.parser')
                post = list(
                    filter(None, map(self.filter_text, soup.stripped_strings))
                )
                item['post'] = '\n'.join(post)
        return self._entries


class GenericParser(ParserFactory):
    """ Generic parser implementation. """
    
    def filter_text(self, text):
        """ Override abstract implementation """
        return super().filter_text(text)
