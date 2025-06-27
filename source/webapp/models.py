from django.db import models

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленные")]


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False, unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Блог'
        verbose_name_plural = "Блоги"


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50, verbose_name='Автор', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=20, verbose_name="Статус", choices=statuses, default=statuses[0][0])
    blog = models.ForeignKey('webapp.Blog', verbose_name="Блог", on_delete=models.RESTRICT, related_name="articles",
                             null=True, blank=True)

    # article_set

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
