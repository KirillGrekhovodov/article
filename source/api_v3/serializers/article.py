from rest_framework import serializers

from api_v3.serializers import TagSerializer
from webapp.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):

    # tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), write_only=True)
    # tags_read = TagSerializer(many=True, read_only=True, source='tags')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'status', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']


    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Длина названия должна быть не менее 5 символов.')
        return value

    def validate(self, attrs):
        return super().validate(attrs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tags'] = TagSerializer(instance.tags.all(), many=True).data
        return data


class ArticleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title']
        read_only_fields = fields
