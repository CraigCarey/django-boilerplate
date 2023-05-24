from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import UserRegistrationForm, UserLoginForm

from .decorators import user_not_authenticated


def home(request):
    return render(request, 'accounts2/home.html')


def sign_up(request):

    if request.method == 'POST':
        # Create a User with data from the request
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/accounts2/home')

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
                return redirect('homepage')

        else:
            for _key, error in list(form.errors.items()):
                messages.error(request, error)

    form = UserLoginForm()

    return render(request=request, template_name='registration/login.html', context={'form': form})
