# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-29 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_card_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_condition',
            field=models.CharField(choices=[('M', 'Mint'), ('NM', 'Near Mint'), ('EX', 'Excellent'), ('GD', 'Good'), ('LP', 'Lightly Played'), ('PL', 'Played'), ('P', 'Poor')], default='NM', max_length=2),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7),
        ),
    ]