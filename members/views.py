from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def loginUser(request):
  page = 'login'
  form = CustomUserLoginForm()
  if request.method == 'POST':
    form = CustomUserLoginForm(data=request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      messages.success(request, 'User logged in successfully')
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'username or password is incorrect')
  context = {'page': page, 'form': form}
  return render(request, 'signupin.html', context)


def logoutUser(request):
  logout(request)
  messages.info(request, 'user was logged out')
  return redirect('login')


def registerUser(request):
  page = 'register'
  form = CustomUserCreationForm()
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      messages.success(request, 'User account was created!')
      return redirect('login')
    else:
      messages.error(request, 'An error occurred during registeration')
  context = {'page': page, 'form': form}
  return render(request, 'signupin.html', context)
