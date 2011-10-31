from piston.handler import BaseHandler

from timeshit.models import TimeshitRecord
from timeshit.forms import *

class TimeshitRecordHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = TimeshitRecord

    @validate(TimeshitRecordForm, 'POST')
    def start(self, request):
        pass

    @validate(TimeshitRecordForm, 'POST')
    def stop(self, request)
        pass
        
