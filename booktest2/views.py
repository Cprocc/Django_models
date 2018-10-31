from django.shortcuts import render
from django.db.models import Max, F, Q
from .models import *
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
