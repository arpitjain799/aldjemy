# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 13:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pg", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tictactoeboard",
            name="board",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(), size=9
            ),
        ),
    ]
