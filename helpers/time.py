import datetime

from timeshit.models import *

def timedelta_to_hours(delta):
    print delta.seconds
    hours = delta.seconds / 3600
    minutes = (delta.seconds % 3600) / 60
    return "%02d:%02d" % (hours, minutes)


def get_today_working_time(user):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

