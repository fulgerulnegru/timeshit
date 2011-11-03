from django.contrib.auth import login as auth_login
from django.contrib.csrf.middleware import csrf_exempt
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from timeshit.decorators import ajax_handler
from timeshit.forms import *
from timeshit.helpers.ajax import *
from timeshit.helpers.auth import *
from timeshit.helpers.time import *


@csrf_exempt
@ajax_handler(TimeshitRecordStartForm, "POST")
def start(request, user, form):
    record = form.save(commit=False)

    if user != record.task.user:
        return ajax_no_perm()

    record.user=user
    record.start_time=datetime.datetime.now()
    record.progress = True
    record.save()
    return ajax_response("Record saved", {
        'model': 'record',
        'id': record.id,
    })


@csrf_exempt
def stop(request):
    user = user_auth(request)
    instance = get_object_or_None(TimeshitRecord, id=request.POST.get('task'), progress=True, user=user)
    if instance is None:
        return ajax_error("Record not found", {}, 1)
    form = TimeshitRecordStopForm(request.POST, instance=instance)

    if form.is_valid():
        record = form.save(commit = False)
        record.progress = False;
        record.end_time = datetime.datetime.now()
        record.cache_duration()
        record = form.save()
        return ajax_response("Record saved", {
            'model': 'record',
            'id': record.id,
            'duration': record.duration,
        })
    return ajax_response("Form is not valid", serialize_form_errors(form), code=1)


def today(request):
    user = user_auth(request)
    seconds = get_today_working_time(user)
    hours = "%02d" % (seconds / 3600)
    minutes = "%02d" % ((seconds % 3600) / 60)
    return render_to_response("records/today.html", {
        'minutes': minutes,
        'hours': hours,
    })
