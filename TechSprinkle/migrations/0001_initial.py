# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=160)),
                ('last_name', models.CharField(max_length=160)),
                ('username', models.CharField(max_length=160)),
                ('email', models.CharField(max_length=160)),
            ],
            options={
                'ordering': ['first_name'],
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'blog_comments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('hashedprojectsid', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('projectname', models.CharField(max_length=160)),
                ('description', models.CharField(max_length=160)),
                ('createdby', models.CharField(max_length=160)),
                ('createddate', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('modifiedby', models.CharField(max_length=160)),
                ('modifieddate', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
                'ordering': ['createddate'],
                'db_table': 'blog_posts',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='hashedprojectsid',
            field=models.ForeignKey(to='TechSprinkle.BlogPost'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='uid',
            field=models.ForeignKey(to='TechSprinkle.User'),
        ),
    ]
