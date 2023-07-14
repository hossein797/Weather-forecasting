from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities:cities')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def sign_in(request):

    return render(request, 'accounts/signin.html')


def change_password(request):
    return render(request, 'accounts/change_password.html')

# TODO:این اپ برای ثبت نام و کار های دیگه کاربران تازه ساخته شده و هیچ کاری هنوز نمیتونه انجام بده.به گیت هم اضافه نشده
