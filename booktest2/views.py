from django.shortcuts import render
from django.db.models import Max, F, Q
from .models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    # book_id_max = BookInfo.books1.aggregate(Max('id'))
    # book_list = BookInfo.books1.filter(heroinfo__h_content__contains='八')

    # 同表引用F对象
    list_read_more_than_comment = BookInfo.books1.filter(b_read__gt=F('b_comment'))

    context = {
        # 'id_max': book_id_max
        # 'list': book_list

        'list': list_read_more_than_comment
    }
    return render(request, 'booktest2/index.html', context)


# 返回一个带有请求连接"localhost:8000/booktest2/...."中参数的内容
def detail(requset, year, month, day):
    return HttpResponse("year:{} month:{} day:{}".format(year, month, day))


def link_page(request):
    return render(request, 'booktest2/link_page.html')


def one_key_one_value(request):
    # request.GET.get()
    # 根据key接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {"a": a1, "b": b1, 'c': c1}
    return render(request, 'booktest2/one_key_one_value.html', context)


def one_key_more_value(request):
    a1 = request.GET.getlist('a')
    context = {"a": a1}
    return render(request, 'booktest2/one_key_more_value.html', context)
