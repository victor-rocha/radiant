# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_radiantpage_mata_description'),
        ('profiles', '0018_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='page',
            field=models.ForeignKey(to='pages.RadiantPage', blank=True, null=True),
        ),
    ]
