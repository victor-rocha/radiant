# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20160124_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='dropdown_thumbnail',
            field=models.ImageField(upload_to='radiant-human/', blank=True),
        ),
    ]
