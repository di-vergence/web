# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tags',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='newapl.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text_tag',
            field=models.CharField(max_length=30),
        ),
    ]
