from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import email_re

from timeshit.models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        super(LoginForm, self).clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            self._errors['email'] = self.error_class(["Your email and/or password were incorrect."])
        elif not user.is_active:
            self._errors['email'] = self.error_class(["Account is not active"])

        self.cleaned_data['user'] = user
        print self.cleaned_data
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def clean_username(self):
        email = self.cleaned_data['email']
        user = get_object_or_None(email = email)

        if not user:
            raise forms.ValidationError('Email already registered')
        return email


