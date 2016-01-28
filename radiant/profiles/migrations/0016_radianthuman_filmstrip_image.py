# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_radianthuman_dropdown_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='filmstrip_image',
            field=models.ImageField(blank=True, upload_to='radiant-human/'),
        ),
    ]
