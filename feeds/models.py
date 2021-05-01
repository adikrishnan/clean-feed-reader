from django.db import models
from django.utils.timezone import now


class FeedSource(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    feed_url = models.URLField(max_length=2000, unique=True)
    last_refreshed = models.DateTimeField(default=now)


class FeedEntry(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.TextField()
    author = models.CharField(max_length=500)
    link = models.URLField()
    summary = models.TextField()
    published = models.DateTimeField()
    updated = models.DateTimeField()
    source = models.ForeignKey(FeedSource, on_delete=models.CASCADE)
    article = models.TextField(null=True, blank=True)
