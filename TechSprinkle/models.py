from __future__ import unicode_literals
from datetime import  datetime
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
import uuid
import json

class User(models.Model):
    first_name=models.CharField(max_length=160)
    last_name=models.CharField(max_length=160)
    username=models.CharField(max_length=160)
    email=models.CharField(max_length=160)
    class Meta:
        managed=False
        db_table ='auth_user'
        ordering = ['first_name']

class BlogPost(models.Model):
    hashedprojectsid = models.UUIDField(primary_key = True,default=uuid.uuid4)
    projectname=models.CharField(max_length=160,blank=False)
    description=models.CharField(max_length=160)
    createdby=models.CharField(max_length=160)
    createddate = models.DateTimeField(default=datetime.now, blank=True)
    modifiedby=models.CharField(max_length=160)
    modifieddate = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        managed=True
        db_table='blog_posts'
        ordering =['createddate']


class BlogComment(models.Model):
    hashedprojectsid = models.ForeignKey(BlogPost)
    uid = models.ForeignKey(User)
    class Meta:
        managed=True
        db_table='blog_comments'

