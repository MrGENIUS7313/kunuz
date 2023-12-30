from django.db import models
from .manager import BaseModels
from ckeditor.fields import RichTextField
from account.models import User
from hitcount.models import HitCountMixin, HitCount
# Create your models here.

class Category(BaseModels):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self) -> str:
        return self.name


class Tags(BaseModels):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'

    def __str__(self) -> str:
        return self.name
    

class News(BaseModels, ):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    body = RichTextField()
    image = models.ImageField(upload_to='news')
    video = models.FileField(upload_to='news_video', null=True, blank=True)
    view_count = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news_category")
    tags = models.ManyToManyField(Tags)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_user")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

    def __str__(self) -> str:
        return self.title