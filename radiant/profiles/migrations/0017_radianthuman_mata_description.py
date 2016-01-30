# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_radianthuman_filmstrip_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='mata_description',
            field=models.CharField(blank=True, max_length=144),
        ),
    ]
