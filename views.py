
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнения не верна'

    form = UserForm()
    context = {'form': form, 'error': error}

    return render(request, 'magazine/index.html', context)


def info(request):
    return render(request, 'magazine/info.html')


def registration(request):
    users = User.objects.order_by("id")
    return render(request, 'magazine/registration.html', {'password': 'Пароль пользователя', users: users})


def checkout(request):
    return render(request, 'magazine/checkout.html')


def history(request):
    return render(request, 'magazine/history.html')
