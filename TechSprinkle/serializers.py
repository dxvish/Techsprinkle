from models import *
from rest_framework import serializers


class User(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username','email')

class BlogPost(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('url', 'hashedprojectsid','projectname','description','createdby','createddate','modifiedby','modifieddate')

class BlogComment(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogComment
        fields = ('url', 'hashedprojectsid','uid')


