from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegistrationForm


def home(request):
    return render(request, 'accounts2/home.html')


def sign_up(request):

    if request.method == 'POST':
        # Create a User with data from the request
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/accounts2/home')

    elif request.method == 'GET':
        # Create an empty form and render it
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
