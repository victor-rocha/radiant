# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160109_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='slider_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
