from django.shortcuts import render, redirect
from django.db.models import Max, F, Q
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from .models import *


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


def post_request_test(request):
    return render(request, 'booktest2/post_request_test.html')


def post_request_test2(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST.get('ugender')
    uhobby=request.POST.getlist('uhobby')
    context = {
        'uname': uname,
        'upwd': upwd,
        'ugender': ugender,
        'uhobby': uhobby}
    return render(request, 'booktest2/post_request_test2.html', context)


def cookie_test(request):
    response = HttpResponse()
    # 拿cookie
    test_cookie = request.COOKIES
    # if 't1' in test_cookie.has_key:
    if 't1' in test_cookie.keys():
        response.write(test_cookie['t1'])
    else:
        response.write("no such cookie")

    # cookies写入之后，再次请求，浏览器的request中就会带上，默认时间是保存两周
    # response.set_cookie('t1', 'abc')
    return response


def redirect1(request):
    # return HttpResponseRedirect('/booktest2/redirect2/')
    return redirect('booktest2/redirect2/')


def redirect2(request):
    return HttpResponse("你是被动来到这里的")


def session1(request):
    context = {'uname': request.session.get('myname', "未登录")}
    return render(request, 'booktest2/session1.html', context)


def session2(request):
    return render(request, 'booktest2/session2.html')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect('/booktest2/session1/')


def session3(request):
    if "myname" in request.session:
        del request.session['myname']
    return redirect('/booktest2/session1')


def get_name(request):
    hero = HeroInfo.objects.get(pk=1)
    context = {'hero': hero}
    return render(request, "booktest2/get_name.html", context)


def show_url(request, use_id):
    context = {"id": use_id}
    return render(request, "booktest2/show_url.html", context)


def basedbase1(request):
    return render(request, "booktest2/basedbase1.html")


def login(request):
    logo = " welcome to zxc's blog "
    return render(request, 'WebHtml/login.html', {'logo': logo})


def documentlist(request):
    logo = " welcome to zxc's blog "
    return render(request, 'WebHtml/documentlist.html', {'logo': logo})


def userpwd(request):
    logo = " welcome to zxc's blog "
    return render(request, 'WebHtml/userpwd.html', {'logo': logo})


def csrf1(request):
    return render(request, 'booktest2/csrf1.html')


def csrf2(request):
    uname = request.POST['uname']
    return render(request, 'booktest2/csrf2.html', {'uname': uname})


def verify_code(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    bg_color = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    im = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(im)
    # point function make some noise
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    str1 = """ABCD123EFGHIJK456LMNOPQRS789TYVWXYZ0"""
    rand_str = ' '
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    font = ImageFont.truetype('symbol.ttf', 23)
    font_color = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, 2), rand_str[0], font=font, fill=font_color)
    draw.text((25, 2), rand_str[1], font=font, fill=font_color)
    draw.text((50, 2), rand_str[2], font=font, fill=font_color)
    draw.text((75, 2), rand_str[3], font=font, fill=font_color)
    del draw
    request.session['verify_code_char'] = rand_str
    from io import StringIO
    buf = StringIO()
    im.save(buf, format('png'))
    return HttpResponse(buf.getvalue(), 'image/png')


def hello_guide(request):
    return render(request, 'WebHtml/HelloStatic.html')


def upload_pic(request):
    return render(request, 'booktest2/upload_pic.html')


def upload_handle(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        f_name = '%s/cars/%s' % (settings.MEDIA_ROOT, f1.name)
        # 定义打开方式wb，则在write函数时可以用二进制写入，不然图片打不开
        with open(f_name, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")


def hero_list_paging(request, p_index=1):
    list_hero = HeroInfo.objects.all()
    paginator = Paginator(list_hero, 5)
    page = paginator.page(int(p_index))
    context = {'page': page}
    return render(request, "booktest2/hero_list_paging.html", context)


def select_area_index(request):
    return render(request, "CityInfo/select_area_index.html")


def get_area1(request):
    area_list = AreaInfo.objects.filter(a_PArea__isnull=True)
    list2 = []
    for a in area_list:
        list2.append([a.a_id, a.a_title])
    return JsonResponse({'data': list2})


def get_area2(request, pid):
    area_list = AreaInfo.objects.filter(a_PArea_id=pid)
    list2 = []
    for a in area_list:
        list2.append({'id': a.a_id, 'title': a.a_title})
    return JsonResponse({'data': list2})


def editor(request):
    return render(request, "other/editor.html")


def content(request):
    h_name = request.POST['h_name']
    h_content = request.POST['h_content']
    hero_info = HeroInfo.objects.get(pk=1)
    hero_info.h_name = h_name
    hero_info.h_content = h_content
    hero_info.save()

    return render(request, 'other/content.html', {'hero': hero_info})


@cache_page(60*10)
def cache1(request):
    return HttpResponse('hello ache')

