from django.urls import path

from webapp.views import UpdateArticleView, DeleteArticleView, ArticleListView, CreateArticleView, DetailArticleView
from webapp.views.comments import CreateCommentView, UpdateCommentView, DeleteCommentView
from webapp.views.projects import ProjectListView, CreateProjectView, DetailProjectView, AddUserInProjectView

app_name = 'webapp'

# webapp:index
urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('add-article/', CreateArticleView.as_view(), name='add-article'),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='article-detail'),
    path('article/<int:pk>/update/', UpdateArticleView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(), name='article-delete'),

    path('article/<int:pk>/add-comment/', CreateCommentView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='comment-delete'),

    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('add-project/', CreateProjectView.as_view(), name='add-project'),
    path('project/<int:pk>/', DetailProjectView.as_view(), name='project-detail'),
    path('project/<int:pk>/add-users/', AddUserInProjectView.as_view(), name='project-add-users'),
]
