from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


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
