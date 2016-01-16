# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20160110_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='radiantpage',
            name='title',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='og_description',
            field=models.CharField(verbose_name='og:description', help_text='Facebook share description', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='og_title',
            field=models.CharField(verbose_name='og:title', help_text='Facebook share title', null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='quote',
            name='radiant_human',
            field=models.ForeignKey(to='pages.RadiantPage', null=True, blank=True),
        ),
    ]
