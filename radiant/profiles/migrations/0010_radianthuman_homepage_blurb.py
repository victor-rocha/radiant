# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20160122_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='homepage_blurb',
            field=models.TextField(null=True, blank=True),
        ),
    ]
