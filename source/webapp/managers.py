from django.db import models
from django.db.models.functions import Coalesce


class ArticleManager(models.Manager):

    def moderated(self):
        return self.filter(status='moderated')


    def comments_count(self):
        return self.annotate(comments_count=Coalesce(models.Count('comments'), 0))