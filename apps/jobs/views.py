from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import bcrypt
from django.http import HttpResponseRedirect


# Create your views here.
def jobs(request):
    user = User.objects.get(id=request.session['id'])
    # boolean = user.admin
    context = {
        "users": User.objects.all(),
        # "boolean": boolean
    }

    return render(request, 'jobs/index.html', context)