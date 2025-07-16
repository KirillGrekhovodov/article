from django.db import models

from webapp.managers import ArticleManager
from webapp.models.base_create_update import BaseCreateUpdateModel

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленные")]


class Article(BaseCreateUpdateModel):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50, verbose_name='Автор', null=False, blank=False)
    status = models.CharField(max_length=20, verbose_name="Статус", choices=statuses, default=statuses[0][0])
    tags = models.ManyToManyField(
        "webapp.Tag",
        verbose_name='Теги',
        related_name='articles',
        blank=True,
        through='webapp.ArticleTag',
        through_fields=("article", "tag"),
    )

    objects = ArticleManager()

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
