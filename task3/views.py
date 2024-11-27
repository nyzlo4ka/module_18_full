from django.shortcuts import render
from django.views.generic import TemplateView


def home_template(request):
    return render(request, 'third_task/home_page.html')


def game_template(request):
    games = {
        'game1': 'Divine Divinity',
        'game2': 'Divinity: Original Sin II',
        'game3': 'Baldur’s Gate 3',
        'game4': 'Dragon Age: Origins',
    }
    context = {'games': games}
    return render(request, 'third_task/shop.html', context)


def cart_template(request):
    return render(request, 'third_task/cart.html')

