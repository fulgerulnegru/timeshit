from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from timeshit.helpers.auth import user_auth
from timeshit.models import *

def new(request):
    return render_to_response('clients/new.html',
                              {},
                              context_instance = RequestContext(request),
                             )


def create(request):
    pass

def index(request):
    user = user_auth(request)
    clients = TimeshitClient.objects.filter(user = user)
    return render_to_response('clients/index.html',
                              {},
                              context_instance = RequestContext(request)
                             )


def show(request, client_id):
    pass


def edit(request, client_id):
    user = user_auth(request)
    client = get_object_or_404(TimeshitClient, id=client_id, user=user)
    return render_to_response('clients/edit.html',
                              {},
                              context_instance = RequestContext(request)
                             )


def delete(request, client_id):
    pass
