from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages


def index(request):
    return render(request, 'handy_helper/index.html')

def register(request):
    userObject = User.objects.isValidRegistration(request.POST)
    if 'user' in userObject:
        request.session['id'] = userObject['user'].id
        request.session['first_name'] = userObject['user'].first_name
        return redirect(reverse('jobs:index'))
    else:
        for error in userObject['errors']:
            messages.warning(request, error)
        return redirect('index')

def login(request):
    userObject = User.objects.isValidLogin(request.POST)
    if 'user' in userObject:
        request.session['id'] = userObject['user'].id
        request.session['first_name'] = userObject['user'].first_name
        return redirect(reverse('jobs:index'))
    else:
        for error in userObject['errors']:
            messages.warning(request, error)
        return redirect('index')

def success(request):
    return render(request, 'handy_helper/index.html')

def logout(request):
    request.session.clear()
    return redirect(reverse('index'))