from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import User
from .models import Job
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import bcrypt
from django.http import HttpResponseRedirect
from django.contrib import messages

def redirect_user_when_invalid_session(request):
    if 'id' not in request.session:
        return redirect("/")

# Create your views here.
def jobs(request):
    if 'id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['id'])
    jobs = Job.objects.all()
    
    context = {
        "jobs": jobs,
    }
    return render(request, 'jobs/index.html', context)

def add_job(request):
    if 'id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['id'])
    return render(request, 'jobs/add_job.html')

def handle_add_job(request):
    user = User.objects.get(id=request.session['id'])
    if request.method =='POST':
        jobObject = Job.objects.isValidRegistration(request.POST, user)
        if 'job' in jobObject:
            return redirect(reverse('jobs:index'))
        else:
            for error in jobObject['errors']:
                messages.warning(request, error)
            return redirect(reverse('jobs:add_job'))

def show_job(request, job_id):
    if 'id' not in request.session:
        return redirect("/")
    job = Job.objects.get(id=job_id)
    user = User.objects.get(id=request.session['id'])
    context = {
        'job' : job,
        'user' : user,
    }
    return render(request, 'jobs/show_job.html', context)

def edit_job(request, job_id):
    if 'id' not in request.session:
        return redirect("/")
    job = Job.objects.get(id=job_id)
    user = User.objects.get(id=request.session['id'])
    context = {
        'job' : job,
        'user' : user,
    }
    if user.id != job.user_id:
        return redirect(reverse('jobs:index'))
    return render(request, 'jobs/edit_job.html', context)


def handle_edit_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method =='POST':
        jobObject = Job.objects.isValidEdit(job, request)
        if 'job' in jobObject:
            return redirect(reverse('jobs:index'))
        else:
            for error in jobObject['errors']:
                messages.warning(request, error)
            return redirect(reverse('jobs:edit_job', args=(job_id,)))