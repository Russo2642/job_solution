from rest_framework import serializers

from .models import Comment, Post, Rating


class RatingReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'field_of_activity', 'title',
            'website', 'location', 'position', 'work_time_from', 'work_time_to', 'body',
            'negative', 'positive', 'ensemble', 'likes_count', 'average_rating', 'created_at',
        )
        read_only_fields = ('id', 'created_at')

    def get_average_rating(self, obj):
        avg_rate = (
                    obj.article_rating.salary +
                    obj.article_rating.team +
                    obj.article_rating.education +
                    obj.article_rating.management +
                    obj.article_rating.social_package +
                    obj.article_rating.office_comfort
                   ) / 6    # noqa: JS102
        return avg_rate

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'author', 'field_of_activity', 'title',
            'website', 'location', 'position', 'work_time_from', 'work_time_to', 'body',
            'negative', 'positive', 'ensemble',
        )


class CommentReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
