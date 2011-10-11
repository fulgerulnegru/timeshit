from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from timeshit.decorators import ajax_handler
from timeshit.forms import *
from timeshit.helpers.ajax import *
from timeshit.helpers.auth import *

def dashboard(request):
    if not request.user.is_authenticated():
        return dashboard_for_annonymous(request)
    return dashboard_for_users(request)


def dashboard_for_users(request):
    user = user_auth(request)
    clients = TimeshitClient.objects.filter(user = user)
    projects = TimeshitProject.objects.filter(user = user)
    tasks = TimeshitTask.objects.filter(user = user)
    return render_to_response('dashboard.html',
                              {
                                  'clients': clients,
                                  'projects': projects,
                                  'tasks': tasks,
                              }, 
                              context_instance = RequestContext(request)
                             )

def dashboard_for_annonymous(request):
    return render_to_response('auth/annonymous.html',
                              {},
                              context_instance = RequestContext(request),
                             )


@ajax_handler(LoginForm)
def login(request, user, form):
    user = form.cleaned_data['user']
    auth_login(request, user)
    return ajax_response("Welcome %s %s" % (user.first_name, user.last_name), {
        'redirectUrl': '/'    
    })


@ajax_handler(RegisterForm)
def register(request):
    return HttpResponse("Okay");

