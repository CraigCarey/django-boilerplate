from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import models

from .models import Invite


class UserRegistrationForm(UserCreationForm):

    class AccountType(models.IntegerChoices):
        FREE = 1
        STANDARD = 2
        PROFESSIONAL = 3

    # Customise the form by adding some fields
    email = forms.EmailField(required=True)
    invite_code = forms.CharField(required=False)
    account_type = forms.ChoiceField(choices=AccountType.choices, required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'invite_code', 'account_type', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.invite_code = self.cleaned_data['invite_code']
        user.account_type = self.cleaned_data['account_type']
        if commit:
            user.save()

        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        min_username_len = 3
        if len(username) <= min_username_len:
            raise forms.ValidationError(f'Username must be at least {min_username_len} characters')
        return username

    def clean_invite_code(self):
        invite_code = self.cleaned_data['invite_code']

        try:
            invite = Invite.objects.get(invite_code=invite_code)
        except ObjectDoesNotExist:
            raise ValidationError(f'"{invite_code}" is not a valid invite code')

        if invite.expiry < datetime.now().date():
            raise ValidationError(f'Invite code "{invite_code}" has expired')

        if invite.use_count >= invite.use_limit:
            raise ValidationError(f'Invite code "{invite_code}" has reached use limit')

        invite.use_count += 1
        invite.save()

        return invite_code


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email'
        }),
        label='Username or Email*'
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
