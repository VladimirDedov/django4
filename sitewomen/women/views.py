from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [{"title": "О сайте", "url_name": "about"},
        {"title":"Добавить статью", "url_name": "addpage"},
        {"title":"Обратная связь", "url_name": "contact"},
        {"title":"Войти", "url_name": "login"}
        ]

def index(request):
    context = {'title': 'Главная страница',
               'menu': menu}
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': 'О сайте!'}
    return render(request, 'women/about.html', context=context)

def show_post(request, post_id):
    return HttpResponse(f'Отображние статьи с id = {post_id}')
def categories(request, cat_slug):
    return HttpResponse(f'Категория: {cat_slug}')

def addpage(request):
    context = {'title': 'Главная страница',
               'menu': menu}
    return HttpResponse('О сайте')

def contact(request):
    context = {'title': 'Главная страница',
               'menu': menu}
    return HttpResponse('Контакты')
def login(request):
    return HttpResponse('login')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Page not found </h1>")
