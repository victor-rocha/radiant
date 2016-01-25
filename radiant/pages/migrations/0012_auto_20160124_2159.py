# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_radiantpage_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radiantpage',
            name='title',
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='template_name',
            field=models.CharField(default='index.html', help_text='Available templates: index.html, about.html, contact.html, radiant-humans.html', max_length=255),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='youtube_url',
            field=models.CharField(help_text='Page name', blank=True, null=True, max_length=255),
        ),
    ]
