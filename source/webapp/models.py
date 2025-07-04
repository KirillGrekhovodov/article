import string
from random import choice

from django.db import models
from pytils.translit import slugify

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленные")]


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    instance_class = instance.__class__
    max_length = 10
    slug = slug[:max_length]
    qs_exists = instance_class.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:max_length - 5], randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug



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
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False, unique=True)
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50, verbose_name='Автор', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=20, verbose_name="Статус", choices=statuses, default=statuses[0][0])
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикация' )
    blog = models.ForeignKey('webapp.Blog', verbose_name="Блог", on_delete=models.RESTRICT, related_name="articles",
                             null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг', null=True, blank=True,)


    def upper_title(self):
        return self.title.upper()


    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)

    # article_set

    def __str__(self):
        return f"{self.id} - {self.title}"


    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
