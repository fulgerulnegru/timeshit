from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from timeshit.helpers.auth import *
from timeshit.decorators import ajax_handler
from timeshit.forms import *
from timeshit.helpers.ajax import *
from timeshit.models import *

def new(request):
    user = user_auth(request)
    clients = TimeshitClient.objects.filter(user = user)
    return render_to_response('projects/new.html',
                              {'clients': clients},
                              context_instance = RequestContext(request))


@ajax_handler(TimeshitProjectForm)
def create(request, user, form):
    project = form.save(commit = False)
    project.user = user
    project.save()
    return ajax_response('Project added', {
        'model': 'project',
        'id': project.id,
        'name': project.name,
        'redirectUrl': '/clients/%s/' % project.client.id
    })


def index(request):
    user = user_auth(request)
    projects = TimeshitProject.objects.filter(user=user)
    return render_to_response('projects/index.html',
                              {'projects': projects},
                              context_instance = RequestContext(request)
                             )


def show(request, project_id):
    user = user_auth(request)
    project = get_object_or_404(TimeshitProject, id=project_id, user=user)
    tasks = TimeshitTask.objects.filter(project = project)
    return render_to_response('tasks/index.html',
                              {'project': project, 'tasks': tasks},
                              context_instance = RequestContext(request)
                             )


def edit(request, project_id):
    user = user_auth(request)
    clients = TimeshitClient.objects.filter(user=user)
    project = get_object_or_404(TimeshitProject, id=project_id, user=user)
    return render_to_response('projects/edit.html',
                              {'project': project,
                               'clients': clients,
                              },
                              context_instance = RequestContext(request)
                             )


def update(request, project_id):
    user = user_auth(request)
    instance = get_object_or_404(TimeshitProject, id = project_id)
    form = TimeshitProjectForm(request.POST, instance = instance)
    if form.is_valid():
        project = form.save(commit = False)
        if project.user != user:
            return ajax_no_perm()
        project.save()
        return ajax_response('Project updated', {
            'model': 'project',
            'id': project.id,
            'name': project.name,
            'redirectUrl': '/clients/%s/' % project.client.id
        });
    return ajax_response("Form is not valid", serialize_form_errors(form), code = 1)


def delete(request):
    pass
