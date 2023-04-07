from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return redirect('error')
            else:
                return redirect('error')

    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})


def error(request):
    return render (request, 'error404.html')