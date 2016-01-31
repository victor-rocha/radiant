# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_auto_20160131_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ('ordering',)},
        ),
        migrations.AddField(
            model_name='teammember',
            name='ordering',
            field=models.IntegerField(default=1),
        ),
    ]
