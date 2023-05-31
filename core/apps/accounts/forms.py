from django import forms
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.db import models
from django.contrib.auth import get_user_model
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


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
