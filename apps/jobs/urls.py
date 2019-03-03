from django.conf.urls import url
from . import views
app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.jobs, name='index'),
    url(r'^/add_job$', views.add_job, name='add_job'),
    url(r'^/handle_add_job', views.handle_add_job, name='handle_add_job'),
    url(r'^/show_job/(?P<job_id>\d+)$', views.show_job, name='show_job'),
    url(r'^/edit_job/(?P<job_id>\d+)$', views.edit_job, name='edit_job'),
    url(r'^/(?P<job_id>\d+)/handle_edit_job$', views.handle_edit_job, name='handle_edit_job'),

]
