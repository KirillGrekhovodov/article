from django.urls import path, include
from rest_framework import routers

from api_v3.views import ArticleViewSet

app_name = 'v3'

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
