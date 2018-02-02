# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(default='', max_length=50)),
                ('content', models.CharField(default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
