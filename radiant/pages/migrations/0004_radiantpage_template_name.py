# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20160109_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='template_name',
            field=models.CharField(default='index.html', help_text='Available templates: index.html, about.html, contact.html', max_length=255),
        ),
    ]
