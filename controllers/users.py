from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from timeshit.forms import *


def dashboard(request):
    return render_to_response('dashboard.html',
                              {},
                              context_instance = RequestContext(request)
                             )

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.cleaned_data['user'])
            return HttpResponseRedirect(reverse('ts__dashboard'))
    else:
        form = LoginForm()
    return render_to_response('auth/login.html',
                              {'form': form},
                              context_instance = RequestContext(request),
                             )

