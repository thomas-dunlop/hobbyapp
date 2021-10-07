from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_protect
import json

@csrf_protect
def render_react_auth(request):
    return render(request, "index.html")

@login_required
@csrf_protect
def render_react(request):
    return render(request, "index.html")

def loginView(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    user = authenticate(username = username, password = password)
    if user is not None: 
        login(request, user)
        url = json.dumps({'url':'/'})
        return HttpResponse(url)
    else:
        return redirect('/login/')

@csrf_protect
def logoutView(request):
    logout(request)
    url = json.dumps({'url':'/login/'})
    return HttpResponse(url)

@csrf_protect
def createAccount(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    user = User.objects.create_user(body['username'], body['email'], body['password'])
    group = Group.objects.get(name = 'Average_Users')
    user.groups.add(group)
    user.save()
    login(request, user)
    url = json.dumps({'url':'/'})
    return HttpResponse(url)