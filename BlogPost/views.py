from django.shortcuts import render
from TechSprinkle.models import *
from BlogPost.models import *
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test

import logging
import os,sys
from django.core import serializers

logger = logging.getLogger()


# @permission_required('request.user.is_superuser', raise_exception=True)

@login_required(login_url='/')
def home(request):
    blogs = BlogPost.objects.all()
    return render(request,'home.html')

def getPosts(request):
    try:
        blogObj=BlogPost.objects.all()
        blogJsonObj = serializers.serialize('json', blogObj)
        return HttpResponse(blogJsonObj)
    except Exception as someerror:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(someerror, exc_type, fname, exc_tb.tb_lineno)
        return HttpResponse("Unable to Save")

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)

@group_required('Edit2')
def savePost(request):
    try:
        print request.POST
        blogtitle = request.POST["json[blogtitle]"]
        description = request.POST["json[description]"]
        blogPost =  BlogPost()
        blogPost.projectname = blogtitle
        blogPost.description = description
        blogPost.createdby = str(request.user.username)
        blogPost.modifiedby = str(request.user.username)
        blogPost.save()
        allProj = BlogPost.objects.all()
        blogJsonObj = serializers.serialize('json', allProj)
        return HttpResponse(blogJsonObj)
    except Exception as someerror:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(someerror, exc_type, fname, exc_tb.tb_lineno)
        return HttpResponse("Unable to Save")
def editPost(request):
    try:
        print request.POST
        hid = request.POST["json[hid]"]
        blogtitle = request.POST["json[blogtitle]"]
        description = request.POST["json[description]"]
        pf = BlogPost.objects.filter(hashedprojectsid=hid).update(projectname=blogtitle,description=description,modifiedby=request.user.username)
        blogPost = BlogPost.objects.get(hashedprojectsid=hid)
        blogJsonObj = serializers.serialize('json', blogPost)
        return HttpResponse(blogJsonObj)
        # return HttpResponse("sadasdsa")
    except Exception as someerror:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(someerror, exc_type, fname, exc_tb.tb_lineno)
        return HttpResponse("Unable to Save")

def deletePost(request):
    try:
        print request.POST
        blogHid = request.POST["json[hid]"]
        proj = BlogPost.objects.filter(hashedprojectsid=blogHid).all()
        proj.delete()
        allProj = BlogPost.objects.all()
        blogJsonObj = serializers.serialize('json', allProj)
        return HttpResponse(blogJsonObj)
    except Exception as someerror:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(someerror, exc_type, fname, exc_tb.tb_lineno)
        return HttpResponse("Unable to Delete ")


