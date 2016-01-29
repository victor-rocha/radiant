# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nominee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('radiant_nominee_name', models.CharField(max_length=255)),
                ('your_name', models.CharField(max_length=255)),
                ('your_email', models.EmailField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='radiant-human/videos/', blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
