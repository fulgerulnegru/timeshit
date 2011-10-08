from django import forms

from timeshit.models import *

class TimeshitClientForm(forms.ModelForm):
    class Meta:
        model = TimeshitClient
        fields = ('name',)

    def clean(self):
        super(TimeshitClientForm, self).clean()
        return self.cleaned_data
