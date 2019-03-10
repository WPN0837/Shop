from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class News(models.Model):
    '''
    新闻
    '''
    title = models.CharField(max_length=1000, null=False, help_text='新闻标题', verbose_name='新闻标题')
    detail = MDTextField(null=False, verbose_name='新闻详情')
    add_time = models.DateField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
