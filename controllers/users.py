from django.shortcuts import render_to_response
from django.template import RequestContext

from timeshit.forms import *


def dashboard(request):
    pass


def login(request):
    if request.method == 'POST':
        form = LoginForm(request)
    else:
        form = LoginForm()
    return render_to_response('auth/login.html',
                              {'form': form},
                              context_instance = RequestContext(request),
                             )

