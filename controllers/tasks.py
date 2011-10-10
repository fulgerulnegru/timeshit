from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from timeshit.helpers.auth import *
from timeshit.decorators import ajax_handler
from timeshit.forms import *
from timeshit.helpers.ajax import *
from timeshit.models import *

def new(request):
    user = user_auth(request)
    projects = TimeshitProject.objects.filter(user = user)
    return render_to_response('tasks/new.html',
                              {'projects': projects},
                              context_instance = RequestContext(request))


@ajax_handler(TimeshitTaskForm)
def create(request, user, form):
    task = form.save(commit = False)
    task.user = user
    task.save()
    return ajax_response('Task added', {
        'model': 'task',
        'id': task.id,
        'name': task.name,
        'redirectUrl': '/projects/%s/' % task.project.id
    })


def index(request):
    user = user_auth(request)
    tasks = TimeshitTask.objects.filter(user=user)
    return render_to_response('tasks/index.html',
                              {'tasks': tasks},
                              context_instance = RequestContext(request)
                             )


def show(request, task_id):
    user = user_auth(request)
    task = get_object_or_404(TimeshitTask, id=project_id, user=user)
    records = TimeshitRecord.objects.filter(task = task)
    return render_to_response('records/index.html',
                              {'task': task, 'records': records},
                              context_instance = RequestContext(request)
                             )


def edit(request, task_id):
    user = user_auth(request)
    projects = TimeshitProject.objects.filter(user=user)
    task = get_object_or_404(TimeshitTask, id=task_id, user=user)
    return render_to_response('tasks/edit.html',
                              {'task': task,
                               'projects': projects,
                              },
                              context_instance = RequestContext(request)
                             )


def update(request, task_id):
    user = user_auth(request)
    instance = get_object_or_404(TimeshitTask, id = task_id)
    form = TimeshitTaskForm(request.POST, instance = instance)
    if form.is_valid():
        task = form.save(commit = False)
        if task.user != user:
            return ajax_no_perm()
        task.save()
        return ajax_response('Task updated', {
            'model': 'task',
            'id': task.id,
            'name': task.name,
            'redirectUrl': '/projects/%s/' % task.project.id,
        });
    return ajax_response("Form is not valid", serialize_form_errors(form), code = 1)


def delete(request):
    pass
