# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RadiantPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, help_text='e.g. Homepage')),
                ('mp4_url', models.CharField(max_length=255, blank=True)),
                ('webm_url', models.CharField(max_length=255, blank=True)),
                ('ogg_url', models.CharField(max_length=255, blank=True)),
                ('content', models.TextField(blank=True)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
