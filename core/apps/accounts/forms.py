from datetime import datetime, timedelta

from django import forms
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Invite, User


# TODO: inherit from UserCreationForm?
class RegisterUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'register-user-form'
        self.helper.add_input(Submit('submit', 'Submit'))

    account_type = forms.ChoiceField(
        choices=User.AccountType.choices,
        widget=forms.Select(
            attrs={
                'hx-get': reverse_lazy('check-account-type'),
                'hx-target': '#div_id_account_type',
                'hx-trigger': 'change',
            }
        ),
    )

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}))

    invite_code = forms.CharField(label='Optional invite code', max_length=128, required=False)

    license_expiry = datetime.now() + timedelta(days=7)

    class Meta:
        model = User
        fields = ('username', 'password', 'date_of_birth', 'account_type', 'invite_code')
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 3:
            raise forms.ValidationError('Username is too short')
        return username

    def clean_account_type(self):
        account_type = self.cleaned_data['account_type']
        if User.objects.filter(account_type=account_type).count() > 3:
            raise forms.ValidationError('There are no spaces on this course')
        return account_type

    def clean_invite_code(self):
        invite_code = self.cleaned_data['invite_code']

        if not invite_code:
            return invite_code

        try:
            invite = Invite.objects.get(invite_code=invite_code)
        except Invite.DoesNotExist:
            raise ValidationError(f'"{invite_code}" is not a valid invite code')

        if invite.expiry < datetime.now().date():
            raise ValidationError('Invite code has expired')

        if invite.use_count >= invite.use_limit:
            raise ValidationError('Invite code has reached use limit')

        invite.use_count += 1
        invite.save()

        return invite_code

    def save(self, commit=True):
        """Hash user's password on save"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'login-user-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('login'),
            'hx-target': '#login-user-form',
            'hx-swap': 'outerHTML',
        }
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }
