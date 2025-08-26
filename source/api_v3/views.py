from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v3.pagination import CustomPageNumberPagination
from api_v3.serializers import ArticleSerializer, ArticleShortSerializer, CommentSerializer
from webapp.models import Article


# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPageNumberPagination
    throttle_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleShortSerializer
        return ArticleSerializer

    @action(detail=True, methods=['GET'], url_path='comments')
    def get_comments(self, request, *args, **kwargs):
        return Response(CommentSerializer(self.get_object().comments.all(), many=True).data)


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})
