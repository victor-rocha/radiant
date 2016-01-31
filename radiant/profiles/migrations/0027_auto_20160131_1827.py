# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_auto_20160131_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radianthuman',
            old_name='homepage_blurb',
            new_name='blurb_image',
        ),
    ]
