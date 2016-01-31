# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_auto_20160131_0828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radianthuman',
            options={'ordering': ('ordering',)},
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='ordering',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
