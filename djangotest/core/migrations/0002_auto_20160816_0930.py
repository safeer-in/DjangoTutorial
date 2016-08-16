# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dept',
            field=models.CharField(default=b'ece', max_length=25, choices=[(b'ece', b'Electronics'), (b'ele', b'Electrical'), (b'mec', b'Mechanical'), (b'civ', b'Civil'), (b'com', b'Computers')]),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=b'st', max_length=100, choices=[(b'st', b'Student'), (b'fc', b'Faculty')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
