from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v3.serializers import ArticleSerializer, ArticleShortSerializer, CommentSerializer
from webapp.models import Article


# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    # def list(self, request, *args, **kwargs):
    #     return Response({"message": "Hello, world!"})


    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleShortSerializer
        return ArticleSerializer


    @action(detail=True, methods=['GET'], url_path='comments')
    def get_comments(self, request, *args, **kwargs):
        return Response(CommentSerializer(self.get_object().comments.all(), many=True).data)

