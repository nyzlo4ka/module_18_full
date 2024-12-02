from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ["Ann", "Max", "Alya"]
    info = {'error': ''}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username in users:
            info["error"] = "Пользователь уже существует!"
        elif password != repeat_password:
            info["error"] = "Пароли не совпадают!"
        elif age < "18":
            info["error"] = "Вы должны быть старше 18!"
        elif username not in users and password == repeat_password and age >= "18":
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "fifth_task/registration_page.html", info)


def sign_up_by_django(request):
    users = ["Ann", "Max", "Alya"]
    info = {'error': ''}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                info["error"] = "Пользователь уже существует!"
            elif password != repeat_password:
                info["error"] = "Пароли не совпадают!"
            elif age < "18":
                info["error"] = "Вы должны быть старше 18!"
            elif username not in users and password == repeat_password and age >= "18":
                return HttpResponse(f"Приветствуем, {username}!")
            else:
                return render(request, "fifth_task/registration_page.html", info)
    else:
        info = {'form': UserRegister()}
    return render(request, "fifth_task/registration_page.html", info)
