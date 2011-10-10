from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from timeshit.decorators import ajax_handler
from timeshit.forms import *


def dashboard(request):
    if not request.user.is_authenticated():
        return dashboard_for_annonymous(request)
    return dashboard_for_users(request)


def dashboard_for_users(request):
    return render_to_response('dashboard.html',
                              {},
                              context_instance = RequestContext(request)
                             )

def dashboard_for_annonymous(request):
    return render_to_response('auth/annonymous.html',
                              {},
                              context_instance = RequestContext(request),
                             )


@ajax_handler(LoginForm)
def login(request, user, form):
    auth_login(request, form.cleaned_data['user'])
    return HttpResponseRedirect(reverse('ts__dashboard'))


@ajax_handler(RegisterForm)
def register(request):
    return HttpResponse("Okay");

