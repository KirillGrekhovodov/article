from django.db import models

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленные")]


class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        abstract = True


class Article(BaseCreateUpdateModel):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50, verbose_name='Автор', null=False, blank=False)
    status = models.CharField(max_length=20, verbose_name="Статус", choices=statuses, default=statuses[0][0])
    tags = models.CharField(max_length=500, verbose_name='Теги', null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"


class Comment(BaseCreateUpdateModel):
    article = models.ForeignKey('webapp.Article', related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"


