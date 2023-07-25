from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# TODO: yekam template ha moshkel dare. git nazadam. har karbar bayad shahr haye khodesh ro dashte bashe

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cities:cities')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cities:cities')
        else:
            return HttpResponse('Invalid login credentials')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('cities:cities')


def change_password(request):
    return render(request, 'accounts/change_password.html')
