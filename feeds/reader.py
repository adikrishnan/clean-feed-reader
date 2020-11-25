from feeds.parser import GenericParser


class FeedReader:
    """ A feed reader that implements Generic Parser. """
    parser_class = GenericParser

    def __init__(self, feed_url, full_post=False):
        self.feed_url = feed_url
        self.full_post = full_post

    def posts(self):
        """ Get all posts. """
        if not getattr(self, 'parser_class', None):
            raise AttributeError('parser_class must be set.')
        parser = self.parser_class(self.feed_url, self.full_post)
        return parser.entries
