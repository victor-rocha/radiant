# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_nominee'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominee',
            name='radiant_nominee_location',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
