# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_radiantpage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='page_image',
            field=models.ImageField(blank=True, upload_to='radiant-pages/'),
        ),
    ]
