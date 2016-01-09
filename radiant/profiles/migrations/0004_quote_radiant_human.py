# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='radiant_human',
            field=models.ForeignKey(blank=True, to='profiles.RadiantHuman', null=True),
        ),
    ]
