# Generated by Django 3.1.3 on 2021-01-04 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('feeds', '0001_initial'), ('feeds', '0002_auto_20210102_0639'), ('feeds', '0003_remove_feedsummary_title_detail'), ('feeds', '0004_feedsources'), ('feeds', '0005_auto_20210104_0704')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedEntry',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('author', models.CharField(max_length=500)),
                ('link', models.URLField()),
                ('summary', models.TextField()),
                ('published', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('source', models.CharField(max_length=200)),
                ('article', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedSource',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('feed_url', models.URLField(max_length=2000)),
                ('last_refreshed', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]