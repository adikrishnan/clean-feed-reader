from django.shortcuts import render
from feeds.reader import FeedReader
from feeds.models import FeedSources


def get_feeds_context(name, reader_class=FeedReader):
    feed = FeedSources.objects.get(name=name)
    posts = reader_class(feed.feed_url).posts()
    context = {
        'posts': posts,
        'title': feed.name,
        'last_refreshed': feed.last_refreshed
    }
    return context


def root(request):
    # TODO: Replace this with autogenerated urls.
    context = {
        'urls': [
            {
                'name': 'Bloomberg Quint',
                'link': '/feed/quint/',
            },
            {
                'name': 'MoneyControl',
                'link': '/feed/moneycontrol/',
            },
            {
                'name': 'Girl With the Jacket',
                'link': '/feed/gwtj/',
            },
        ],
        'title': 'Feed List',
    }
    return render(request, 'feed_list.html', context=context)


def quint_reader_view(request):
    context = get_feeds_context('Bloomberg Quint')
    return render(request, 'feed_reader.html', context)


def gwtj_reader_view(request):
    context = get_feeds_context('Girl With the Jacket')
    return render(request, 'feed_reader.html', context)


def moneycontrol_reader_view(request):
    context = get_feeds_context('MoneyControl - Top News')
    return render(request, 'feed_reader.html', context)
