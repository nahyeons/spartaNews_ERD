from .models import Article
from rest_framework import serializers


# 게시글 목록 시리얼라이저
class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source="User.username"
    )  # 작성자는 읽기전용으로 / 'source=' 으로 username만 가져옴

    class Meta:
        model = Article
        fields = [
            "title",
            "url",
            "content",
            "author",
            "created_at",
        ]
        read_only_fields = ('created_at', )

        
