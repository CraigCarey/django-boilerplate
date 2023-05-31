from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .forms import UserRegistrationForm, UserLoginForm

from .decorators import user_not_authenticated


def home(request):
    return render(request, 'accounts/home.html')


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (str(user.pk) + str(timestamp) + str(user.is_active))


account_activation_token = AccountActivationTokenGenerator()


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('activate-done')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('homepage')


def activate_done(request):
    return render(request, 'registration/activate_account_done.html')


def activate_waiting(request):
    return render(request, 'registration/activate_account_waiting.html')


def _activate_email(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string(
        'registration/activate_account_email.html', {
            'user': user.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http'
        }
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.'
        )
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def sign_up(request):

    if request.method == 'POST':
        # Create a User with data from the request
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            _activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('/activate/waiting')

    elif request.method == 'GET':
        # Create an empty form and render it
        form = UserRegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})


@user_not_authenticated
def custom_login(request):

    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Hello <b>{user.username}</b>! You have been logged in')
                return redirect('home')

        else:
            for _key, error in list(form.errors.items()):
                messages.error(request, error)

    form = UserLoginForm()

    return render(request=request, template_name='registration/login.html', context={'form': form})
