from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from BlogPost import views
from django.http import *
from cryptography.fernet import Fernet
from django.conf import settings


def loginPage(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def authenticateUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # if user.is_superuser:
                return HttpResponseRedirect('/blog/list/')
            else:
                return HttpResponseRedirect('/')
        else:
            return render(request,'login.html')


def change_password(request):
    template_response = views.password_change(request)
    return template_response

def encryption(text):
    f = Fernet(settings.ENCRYPT_KEY)
    encrypted_text  = f.encrypt(text)
    return encrypted_text

def decryption(cipher_text):
    f = Fernet(settings.ENCRYPT_KEY)
    plain_text = f.decrypt(cipher_text)
    return plain_text


# def handler404(request):
#     response = render_to_response('404.html', {},context_instance=RequestContext(request))
#     response.status_code = 404
#     return response

