# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_radianthuman_mata_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('role', models.IntegerField(choices=[(1, 'Directors'), (2, 'Editor'), (3, 'Developers'), (4, 'Designer')])),
                ('thumbnail', models.ImageField(blank=True, upload_to='team/')),
                ('blurb', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
