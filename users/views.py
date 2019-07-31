from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created Successfully! You are now able to login')
            return redirect('login')

    else:
        form = UserRegisterForm()

    register_page = loader.get_template('register.html')
    return HttpResponse(register_page.render({'form': form}, request), )

