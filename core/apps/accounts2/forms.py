from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class RegistrationForm(UserCreationForm):

    class AccountType(models.IntegerChoices):
        FREE = 1
        STANDARD = 2
        PROFESSIONAL = 3

    # Customise the form by adding a field
    email = forms.EmailField(required=True)
    dietary_requirements = forms.CharField(required=False)
    account_type = forms.ChoiceField(choices=AccountType.choices, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'dietary_requirements', 'account_type', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        min_username_len = 3
        if len(username) <= min_username_len:
            raise forms.ValidationError(f'Username must be at least {min_username_len} characters')
        return username
