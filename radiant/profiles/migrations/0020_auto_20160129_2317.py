# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_teammember_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='role',
            field=models.IntegerField(choices=[(1, 'Director'), (2, 'Editor'), (3, 'Developer'), (4, 'Designer')]),
        ),
    ]
