from django.shortcuts import render_to_response
from django.template import RequestContext

from timeshit.decorators import ajax_handler

def new(request):
    return render_to_response('projects/new.html',
                              {},
                              context_instance = RequestContext(request))


@ajax_handler(TimeshitProjectForm)
def create(request, user, form):
    pass


def show(request, project_id):
    pass

