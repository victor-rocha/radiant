# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20160131_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiantpage',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
