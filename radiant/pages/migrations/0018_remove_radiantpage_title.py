# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_radiantpage_mata_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radiantpage',
            name='title',
        ),
    ]
