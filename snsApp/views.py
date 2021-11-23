from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupFunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    try:
        User.objects.create_user(username, '', password)
        return render(request, 'signup.html', {'some': 100})
    except IntegrityError:
        return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
  return render(request, 'signup.html', {'some': 100})

def loginFunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('list')
    else:
        return render(request, 'login.html', {})
  return render(request, 'login.html', {})

@login_required
def listFunc(request):
  object_list = BoardModel.objects.all()
  return render(request, 'list.html', {'object_list': object_list})

def logoutFunc(request):
  logout(request)
  return redirect('login')
