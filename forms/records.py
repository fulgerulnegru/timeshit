import datetime
from django import forms
from annoying.functions import get_object_or_None
from timeshit.models import *

class TimeshitRecordStartForm(forms.ModelForm):
    class Meta:
        model = TimeshitRecord
        fields = ('task',)

    def clean(self):
        super(TimeshitRecordStartForm, self).clean()
        return self.cleaned_data

    def clean_task(self):
        task = self.cleaned_data['task']
        user = task.user
        print task

        if TimeshitRecord.objects.filter(user=user, progress=True):
            raise forms.ValidationError('There is a record in progress')
        return self.cleaned_data['task']


class TimeshitRecordStopForm(forms.ModelForm):
    class Meta:
        model = TimeshitRecord
        fields = ('task',)

    def clean(self):
        super(TimeshitRecordStopForm, self).clean()
        return self.cleaned_data

    def clean_task(self):
        task = self.cleaned_data['task']
        user = task.user

        record = get_object_or_None(TimeshitRecord, user=user, progress=True, task=task)
        if not record:
            raise forms.ValidationError("There is no record in progress")
        return self.cleaned_data['task']
