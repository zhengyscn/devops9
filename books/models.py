from django.db import models

# Create your models here.



class Publish(models.Model):
    '''
    出版商
    '''

    name    =   models.CharField(max_length=32, verbose_name='出版商名称', help_text='出版商名称')
    city    =   models.CharField(max_length=32, null=True, blank=True, verbose_name='出版商城市', help_text='出版商名称')
    address =   models.CharField(max_length=32, null=True, blank=True, verbose_name='出版商地址', help_text='出版商地址')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name



class Author(models.Model):
    '''
    作者
    '''

    name    =   models.CharField(max_length=32, verbose_name='作者名称', help_text='作者名称')
    email   =   models.EmailField(verbose_name='邮箱', help_text='邮箱')
    phone   =   models.CharField(max_length=11, verbose_name='手机号', help_text='手机号')
    city    =   models.CharField(max_length=100, null=True, blank=True, verbose_name='城市', help_text='城市')
    address =   models.CharField(max_length=100, null=True, blank=True, verbose_name='作者地址', help_text='作者地址')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name



class Book(models.Model):
    '''
    图书
    '''

    name        =   models.CharField(max_length=100, verbose_name='书名', help_text='书名')
    # 作者 和 书 是多对多的关系
    author      =   models.ManyToManyField(Author, verbose_name='作者', help_text='作者')
    # 一本书只能被一家出版商出版，一家出版商可以出版很多书
    # on_delete https://blog.csdn.net/lht_521/article/details/80605146
    publisher   =   models.ForeignKey(Publish, on_delete=models.CASCADE, verbose_name='出版社', help_text='出版商')
    publication_date =   models.DateTimeField(null=True, blank=True, verbose_name='出版时间', help_text='出版时间')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name