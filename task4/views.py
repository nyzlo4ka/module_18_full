from django.shortcuts import render


def home_template(request):
    return render(request, 'fourth_task/home_page.html')


def game_template(request):
    title = "Games"
    name = "Игры"
    button = "Купить"
    games = ['Divine Divinity', 'Divinity: Original Sin II',
             'Baldur’s Gate 3', 'Dragon Age: Origins']
    context = {
        'title': title,
        'name': name,
        'button': button,
        'games': games,

    }
    return render(request, 'fourth_task/shop.html', context)


def cart_template(request):
    return render(request, 'fourth_task/cart.html')


def menu_template(request):
    return render(request, 'fourth_task/menu.html')

