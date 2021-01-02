from django.shortcuts import render
from feeds.reader import FeedReader

# Create your views here.


def livemint_reader_view(request):
    mint_url = 'https://www.livemint.com/rss/opinion'
    posts = FeedReader(mint_url).posts()
    context = {'posts': posts}
    return render(request, 'feed_reader.html', context)


def quint_reader_view(request):
    quint_url = 'https://www.bloombergquint.com/stories.rss'
    posts = FeedReader(quint_url).posts()
    context = {'posts': posts}
    return render(request, 'feed_reader.html', context)


def gwtj_reader_view(request):
    gwtj_url = 'https://girlwiththejacket.wordpress.com/feed/'
    posts = FeedReader(gwtj_url).posts()
    context = {'posts': posts}
    return render(request, 'feed_reader.html', context)
