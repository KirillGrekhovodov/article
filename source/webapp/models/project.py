from django.contrib.auth import get_user_model
from django.db import models


from webapp.models.base_create_update import BaseCreateUpdateModel


class Project(BaseCreateUpdateModel):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    users = models.ManyToManyField(get_user_model(), related_name="projects", blank=True)

    class Meta:
        db_table = 'projects'
        permissions = [("add_users_in_project", "Добавлять пользователей в проект")]
