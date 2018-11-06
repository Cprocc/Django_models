from django.contrib import admin
from .models import BookInfo
from .models import HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['b_title', "b_pub_date"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
