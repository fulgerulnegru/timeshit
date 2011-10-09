from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from timeshit.decorators import ajax_handler
from timeshit.helpers.auth import user_auth
from timeshit.helpers.ajax import *
from timeshit.forms import *
from timeshit.models import *

def new(request):
    return render_to_response('clients/new.html',
                              {},
                              context_instance = RequestContext(request),
                             )


@ajax_handler(TimeshitClientForm)
def create(request, user, form):
    client = form.save(commit = False)
    client.user = user
    client.save()
    return ajax_response('Client added', {
        'model': 'client',
        'id': client.id,
        'name': client.name,
        'redirectUrl': '/clients/',
    })


def index(request):
    user = user_auth(request)
    clients = TimeshitClient.objects.filter(user = user)
    return render_to_response('clients/index.html',
                              {'clients': clients},
                              context_instance = RequestContext(request)
                             )


def show(request, client_id):
    user = user_auth(request)
    client = get_object_or_404(TimeshitClient, id = client_id, user = user)
    projects = TimeshitProject.objects.filter(client = client)
    return render_to_response('projects/index.html',
                              {'client': client, 'projects': projects},
                              context_instance = RequestContext(request))


def edit(request, client_id):
    user = user_auth(request)
    client = get_object_or_404(TimeshitClient, id=client_id, user=user)
    return render_to_response('clients/edit.html',
                              {'client': client},
                              context_instance = RequestContext(request)
                             )


def update(request, client_id):
    user = user_auth(request)
    instance = get_object_or_404(TimeshitClient, id=client_id)
    form = TimeshitClientForm(request.POST, instance = instance)
    if form.is_valid():
        client = form.save(commit = False)
        if client.user != user:
            return ajax_no_perm()
        client.save()
        return ajax_response('Client updated', {
            'model': 'client',
            'id': client.id,
            'name': client.name,
            'redirectUrl': '/clients/',
        })
    return ajax_response("Form is not valid", serialize_form_errors(form), code = 1)


def delete(request, client_id):
    pass
