from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):
    data = {'title': 'Head page',
            'menu': menu,
            'posts': data_db,
            'cat_selected': 0
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'title': 'About page',
            'menu': menu}
    return render(request, 'women/about.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f"Пост номер {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    data = {'title': 'Отображение по рубрикам',
            'menu': menu,
            'posts': data_db,
            'cat_selected': int(cat_slug),
            }

    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Page not found </h1>")
