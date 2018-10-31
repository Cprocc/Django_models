from django.db import models

# Create your models here.

# 更改标的结构一定要重新迁移，迁移的表最好是空的


# 改写默认的manage方法，改写get_queryset方法，更改默认的查询操作，可以配合filter过滤
# 调用all()方法，就会体现出get_queryset的区别
class BookInfoManage(models.Manager):
    def get_queryset(self):
        return super(BookInfoManage, self).get_queryset().filter(isDelete=False)

    # 再管理器中自定义创建模型类的方法
    def create_book(self, title, pub_date):
        # book = self.model()
        # book.b_title = title
        # book.b_pub_date = pub_date
        # book.b_read = 0
        # book.b_comment = 0
        # book.isDelete = False

        # 免除save()过程的一种方法
        book = self.create(b_title=title, b_pub_date=pub_date,
                           b_read=0, b_comment=0, isDelete=False)
        return book


class BookInfo(models.Model):
    b_title = models.CharField(max_length=20)
    b_pub_date = models.DateTimeField()
    b_read = models.IntegerField(default=0)
    b_comment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    # 用类方法，模拟类的自定义。因为__init__方法已经被model中使用
    # 不推荐的用法
    @classmethod
    def create(cls, title, pub_date):
        book = cls(b_title=title, b_pub_date=pub_date)
        book.b_read = 0
        book.b_comment = 0
        book.isDelete = False
        return book

    class Meta:
        # 可以不指定，这样的话db_table是app的名字加上类的名字
        db_table = 'book_info'
        # 可以定义默认排序方式但是会增加数据库的开销
        # ordering = ['id']

    # 测试两个管理器的不同
    books1 = models.Manager()
    books2 = BookInfoManage()


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    h_content = models.CharField(max_length=100)
    h_book = models.ForeignKey('BookInfo', on_delete=True)
