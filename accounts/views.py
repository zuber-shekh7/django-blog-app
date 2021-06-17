from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserSignInForm


def signin(request):
    form = UserSignInForm()
    context = {
        "form": form,
    }
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'{username} login successful')
                return redirect('core:index')
    return render(request, 'accounts/signin.html', context)


def signup(request):
    form = UserRegisterForm()
    context = {
        "form": form,
    }
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}')
            return redirect('core:index')
    return render(request, 'accounts/signup.html', context)
