from django import forms

from timeshit.models import *

class TimeshitProjectForm(forms.ModelForm):
    class Meta:
        model = TimeshitProject
        fields = ('name', 'client',)

    def clean(self):
        super(TimeshitProjectForm, self).clean()
        return self.cleaned_data
