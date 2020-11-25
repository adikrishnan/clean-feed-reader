from django.shortcuts import render
from feeds.reader import FeedReader

# Create your views here.

def feed_reader_view(request):
    mint_url = 'https://www.livemint.com/rss/opinion'
    posts = FeedReader(mint_url, full_post=True).posts()
    context = {'posts': posts}
    return render(request, 'feed_reader.html', context)

