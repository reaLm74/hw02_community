from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name="Название группы", max_length=200)
    slug = models.SlugField(verbose_name="Адрес страницы группы", unique=True)
    description = models.TextField(verbose_name="Описание группы")

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Название статьи")
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='groups'
    )

    class Meta:
        ordering = ('-pub_date',)
