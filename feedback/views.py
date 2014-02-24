from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.flatpages.models import FlatPage
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from feedback.forms import FeedbackForm

def leave_feedback(request, template_name='contacts.html'):
    contacts = FlatPage.objects.get(url=request.path)
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.save()
        message = "Your feedback was submitted."
        cd = form.cleaned_data
        send_mail(
                '%s(%s)'%(cd['name'], cd['phone']),
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['shkipc@gmail.com'])
        #redirecting back
        return HttpResponseRedirect(request.POST.get('next', request.META.get('HTTP_REFERER', '/')))
        # return render_to_response(template_name, {'next' : request.GET.get('next', '/'), 'feedback_form': FeedbackForm(None), 'mes':message}, context_instance=RequestContext(request))
    return render_to_response(template_name, {'feedback_form': form, 'contacts': contacts}, context_instance=RequestContext(request))

def thanks(request):
    return render(request, 'thanks.html')