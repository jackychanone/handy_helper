from django.db import models
from django.db import models
import datetime

class JobManager(models.Manager):
    def isValidRegistration(self, jobInfo, user):
        registrationObject = {
            "errors": []
        }
        validRegistration = True
        if len(jobInfo['title']) < 3:
            registrationObject['errors'].append('Title must be at least 3 char.')
            validRegistration = False
        if len(jobInfo['description']) < 10:
            registrationObject['errors'].append('Description must be at least 10 char.')
            validRegistration = False
        if len(jobInfo['location']) == 0:
            registrationObject['errors'].append('Location must not be blank!')
            validRegistration = False

        if validRegistration:
            new_job = Job.objects.create(title = jobInfo['title'], description = jobInfo['description'], location = jobInfo['location'], user = user)
            registrationObject['job'] = new_job
        return registrationObject 

    def isValidEdit(self, jobInfo, request):
        editObject = {
            "errors": []
        }
        validEdit = True
        if len(request.POST['title']) < 3:
            editObject['errors'].append('Title must be at least 3 char.')
            validEdit = False 
        if len(request.POST['description']) < 10:
            editObject['errors'].append('Description must be at least 10 char.')
            validEdit = False
        if len(request.POST['location']) == 0:
            editObject['errors'].append('Location must not be blank!')
            validEdit = False
        if validEdit:
            jobInfo.title = request.POST['title']
            jobInfo.description = request.POST['description']
            jobInfo.location = request.POST['location']
            jobInfo.save()
            editObject['job'] = jobInfo
        return editObject
        

class Job(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('login_registration.user', related_name='user_jobs')
    objects = JobManager()
    
