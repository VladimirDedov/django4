from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    context = {'title': 'Главная страница',
               'menu': menu}
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': 'О сайте!'}
    return render(request, 'women/about.html', context=context)


def categories(request, cat_slug):
    return HttpResponse(f'Категория: {cat_slug}')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Page not found </h1>")
