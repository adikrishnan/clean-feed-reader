from django.db import models


# Create your models here.
class FeedSummary(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.TextField()
    author = models.CharField(max_length=500)
    link = models.URLField()
    summary = models.TextField()
    published = models.DateTimeField()
    updated = models.DateTimeField()
    source = models.CharField(max_length=200)


class FeedDetail(models.Model):
    id = models.UUIDField(primary_key=True)
    post = models.TextField(null=True, blank=True)
    feed_summary = models.ForeignKey('FeedSummary', on_delete=models.DO_NOTHING)
