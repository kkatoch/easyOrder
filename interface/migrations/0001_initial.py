# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 13:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('amount', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Processing'), (2, 'Failed'), (3, 'Completed')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=4096, null=True, verbose_name='Restaurant Name')),
                ('info', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(choices=[(0, 'Unrated'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.Restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
