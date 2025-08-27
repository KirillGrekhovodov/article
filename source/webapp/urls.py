from django.urls import path

from webapp.views import UpdateArticleView, DeleteArticleView, ArticleListView, CreateArticleView, DetailArticleView
from webapp.views.articles import ArticleLikeView, TestFormView
from webapp.views.comments import CreateCommentView, UpdateCommentView, DeleteCommentView, CommentLikeView

app_name = 'webapp'

#webapp:index
urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('add-article/', CreateArticleView.as_view(), name='add-article'),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='article-detail'),
    path('article/<int:pk>/update/', UpdateArticleView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(), name='article-delete'),

    path('article/<int:pk>/add-comment/', CreateCommentView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='comment-delete'),

    path('article/<int:pk>/like/', ArticleLikeView.as_view(), name='article-like'),
    path('comment/<int:pk>/like/', CommentLikeView.as_view(), name='comment-like'),
    path('test-form/', TestFormView.as_view(), name='test-form'),
]
