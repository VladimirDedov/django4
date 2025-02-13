from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'women/index.html' )


def categories(request, cat_slug):
    # st=''
    # if request.GET:
    #     for query in request.GET.items():
    #         st+=str(query[0])+'='+str(query[1])+'|'
    #     print(st.strip('|'))
    # else:
    #     print("Пустая юля")

    print(f'Zapros {request.GET}')
    return HttpResponse(f'Категория: {cat_slug}')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Page not found </h1>")
