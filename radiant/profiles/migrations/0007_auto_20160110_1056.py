# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_radianthuman_slider_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='release_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (2, 'Unreleased'), (1, 'Live')], default=0),
        ),
    ]
