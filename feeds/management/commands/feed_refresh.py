from django.core.management.base import BaseCommand, CommandError
from feeds.utils import feed_refresh


class Command(BaseCommand):
    help = 'Refreshes data in the DB'

    def handle(self, *args, **kwargs):
        try:
            feed_refresh()
        except Exception as ex:
            raise CommandError(f'Processing failed due to error: {ex}')
