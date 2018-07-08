from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegistrationForm, ShopUserEditForm


def login(request):
    title = 'Login'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def edit(request):
    title = 'Account'
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {'title': title, 'edit_form': edit_form}

    return render (request, 'authapp/edit.html', context)


def registration(request):
    title = 'Registration'

    if request.method == 'POST':
        registration_form = ShopUserRegistrationForm(request.POST, request.FILES)
        print(registration_form.error_class)
        if registration_form.is_valid():
            print(2)
            registration_form.save()
            print(3)
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        registration_form = ShopUserRegistrationForm()

    context = {
        'title': title,
        'registration_form': registration_form
    }

    return render(request, 'authapp/registration.html', context)
