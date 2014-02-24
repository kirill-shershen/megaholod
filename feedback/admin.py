# -*- coding:utf-8 -*-
from django.contrib import admin
from django.conf.urls import *
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    # def view(self, obj):
    #     """
    #     returns link to feedback
    #     """
    #     return "<a href='%s'>View</a>" % obj.get_absolute_url()

    # view.allow_tags = True
    
    list_display = ['name', 'email', 'message', 'time']
    search_fields = ['email', 'message']
    list_filter = ['name', 'time']
    
    # def get_urls(self):
    #     urls = super(FeedbackAdmin, self).get_urls()
    #     my_urls = patterns('',
    #         url(r'^view/(?P<feedback_id>\d+)/$', self.admin_site.admin_view(self.view_feedback), name='view-feedback'),
    #     )
    #     return my_urls + urls
        
    # def view_feedback(self, request, feedback_id):
    #     """
    #     gets feedback by id and renders it
    #     """
    #     feedback = get_object_or_404(Feedback, id=feedback_id)
    #     return render_to_response('feedback/view_feedback.html',
    #         {'feedback': feedback}, context_instance=RequestContext(request))

admin.site.register(Feedback, FeedbackAdmin)
# admin.site.index_template = 'feedback/index.html'