# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20160129_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='website',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
