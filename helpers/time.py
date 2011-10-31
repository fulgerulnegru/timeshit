import datetime

from timeshit.models import *

def timedelta_to_hours(delta):
    print delta.seconds
    hours = delta.seconds / 3600
    minutes = (delta.seconds % 3600) / 60
    return "%02d:%02d" % (hours, minutes)


def get_today_working_time(user):
    today_date = datetime.date.today()
    today = datetime.datetime(
        year = today_date.year,
        month = today_date.month,
        day = today_date.day
    )
    records = TimeshitRecord.objects.filter(
        end_time__gte = today,
        user = user
    )
    seconds = 0
    for record in records:
        start_time = record.start_time if record.start_time >= today else today
        seconds += (record.end_time - start_time).seconds
    return seconds

