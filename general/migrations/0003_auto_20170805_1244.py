# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_page_card_block'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customcontent',
            options={'ordering': ['title'], 'verbose_name': 'custom content module'},
        ),
    ]
