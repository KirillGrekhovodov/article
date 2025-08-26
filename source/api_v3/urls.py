from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api_v3.views import ArticleViewSet, LogoutView

app_name = 'v3'

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view(),)
]
