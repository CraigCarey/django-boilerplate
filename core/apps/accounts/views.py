from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .decorators import user_not_authenticated
from .forms import UserLoginForm, UserRegistrationForm


def home(request):
    return render(request, 'accounts/home.html')


def profile(request):
    return render(request, 'accounts/profile.html')


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)


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

        messages.success(
            request,
            'Thank you for your confirming your emil address. You may now log in to your account.',
        )
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid')

    return redirect('home')


def activate_done(request):
    return render(request, 'registration/activate_account_done.html')


def _activate_email(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string(
        'registration/activate_account_email.html',
        {
            'user': user.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http',
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request,
            f'<b>{user}</b>, please go to your email inbox and follow the  \
            received activation link to confirm and complete the registration. \
            <b>Note:</b> You may need to check your spam folder.',
        )
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}')


def sign_up(request):

    if request.method == 'POST':
        # Create a User with data from the request
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            _activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('login')

    elif request.method == 'GET':
        # Create an empty form and render it
        form = UserRegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})


def message_demo(request):
    messages.debug(request, 'debug message')
    messages.info(request, 'info message')
    messages.success(request, 'success message')
    messages.warning(request, 'warning message')
    messages.error(request, 'error message')

    return redirect('profile')


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
                messages.success(request, f'Hello <b>{user.username}</b>. You have been logged in')
                return redirect('home')

        else:
            for _key, error in list(form.errors.items()):
                messages.error(request, error)

    form = UserLoginForm()

    return render(request=request, template_name='registration/login.html', context={'form': form})
