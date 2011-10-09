from django import forms

from timeshit.models import *

class TimeshitTaskForm(forms.ModelForm):
    class Meta:
        model = TimeshitTask
        fields = ('name', 'project',)

    def clean(self):
        super(TimeshitTaskForm, self).clean()
        return self.cleaned_data
