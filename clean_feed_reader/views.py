from django.http import HttpResponse
from django.shortcuts import render
from feeds.models import FeedEntry, FeedSource
from feeds.utils import feed_refresh


def load_objects(request):
    """ Load objects from source to DB """
    # Handle duplicates
    try:
        feed_refresh()
        return HttpResponse('Loaded objects')
    except Exception:
        return HttpResponse('Failed to refresh')


def root(request):
    sources = FeedSource.objects.all()
    urls = [
        {'name': source.name, 'link': source.url_slug} for source in sources
    ]
    entries_count = FeedEntry.objects.all().count()
    context = {
        'urls': urls,
        'title': 'Feed List',
        'entries': entries_count,
    }
    return render(request, 'feed_list.html', context=context)


def reader_view(request, slug):
    source = FeedSource.objects.get(url_slug=slug)
    entries = FeedEntry.objects.filter(source=source.id)
    context = {
        'posts': entries,
        'title': source.name,
    }
    return render(request, 'feed_reader.html', context)
