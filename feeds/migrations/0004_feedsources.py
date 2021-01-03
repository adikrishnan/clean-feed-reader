# Generated by Django 3.1.3 on 2021-01-03 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_remove_feedsummary_title_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedSources',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('feed_url', models.URLField(max_length=2000)),
                ('last_refreshed', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
