from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import email_re

from timeshit.models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email_re.match(email):
            raise forms.ValidationError("Email is not valid")
        return email

    def clean(self):
        email = self.cleaned_data['email'] if 'email' in self.cleaned_data else None
        password = self.cleaned_data['password'] if 'password' in self.cleaned_data else None

        user = authenticate(email=email, password=password)

        if user is None:
            self._errors['username'] = self.error_class(["Your username and/or password were incorrect."])
        elif not user.is_active:
            self._errors['username'] = self.error_class(["Username is not active"])

        return self.cleaned_data
