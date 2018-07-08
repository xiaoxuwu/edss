# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='looking_for',
            field=models.CharField(choices=[('IN', 'Interns'), ('FT', 'Full-time'), ('B', 'Both')], default='IN', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='space',
            field=models.CharField(choices=[('P', 'Patio Exhibition'), ('PS_2', 'Premium Space, 2 Tables'), ('PS_1', 'Premium Space, 1 Table'), ('SS_2', 'Standard Space, 2 Tables'), ('SS_1', 'Standard Space, 1 Table')], default='P', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='rep_2_email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='rep_2_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='rep_2_phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='company',
            name='special_needs',
            field=models.TextField(blank=True),
        ),
    ]
