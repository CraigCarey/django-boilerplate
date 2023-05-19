from .forms import RegisterUserForm

from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from crispy_forms.utils import render_crispy_form

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'GET':
        context = {'form': RegisterUserForm()}
        return render(request, 'register.html', context)

    elif request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            response = redirect(reverse_lazy('profile'))
            return response

        ctx = {}
        ctx.update(csrf(request))
        form_html = render_crispy_form(form, context=ctx)
        return HttpResponse(form_html)


def check_username(request):
    form = RegisterUserForm(request.GET)
    context = {
        'field': as_crispy_field(form['username']),
        'valid': not form['username'].errors,
    }
    return render(request, 'partials/field.html', context)


def check_account_type(request):
    form = RegisterUserForm(request.GET)
    context = {
        'field': as_crispy_field(form['account_type']),
        'valid': not form['account_type'].errors,
    }
    return render(request, 'partials/field.html', context)


@login_required
def profile(request):
    template = render(request, 'profile.html')
    return template
