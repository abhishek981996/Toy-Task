# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0002_auto_20180224_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='caseTitle',
            field=models.CharField(max_length=50),
        ),
    ]
