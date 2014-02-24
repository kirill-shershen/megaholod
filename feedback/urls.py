from django.conf.urls import *
from feedback.views import leave_feedback, thanks

urlpatterns = patterns('',
    url(r'^$', leave_feedback, name='leave-feedback'),
    url(r'^thanks/$', thanks, name='thanks'),
)