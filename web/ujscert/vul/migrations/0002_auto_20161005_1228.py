# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-05 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vul', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('vul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vul.Vul')),
                ('content', models.CharField(max_length=1024)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vul.WhiteHat')),
            ],
        ),

        migrations.CreateModel(
            name='LikeForComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vul.WhiteHat')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vul.Comment')),
            ],
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='user',
        ),
        migrations.AlterField(
            model_name='timeline',
            name='event_type',
            field=models.IntegerField(choices=[(0, '更新状态'), (1, '奖励变动')], default=0),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='timestamp',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='vul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vul.Vul'),
        ),
        migrations.AlterField(
            model_name='vul',
            name='status',
            field=models.IntegerField(choices=[(0, '待审核'), (1, '已确认'), (2, '已忽略'), (3, '待复核'), (4, '已修复'), (5, '已公开')], default=0),
        ),
    ]