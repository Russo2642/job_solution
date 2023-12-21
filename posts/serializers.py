from rest_framework import serializers

from .models import Comment, Post, Rating


class RatingReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'


class RatingWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = '__all__'


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    views_count = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'field_of_activity', 'title',
            'company', 'website', 'location', 'position', 'work_time_from', 'work_time_to', 'body',
            'negative', 'positive', 'ensemble',
            'likes_count', 'views_count', 'comments_count', 'average_rating', 'created_at',
        )
        read_only_fields = ('id', 'created_at')

    def get_average_rating(self, obj):
        avg_rate = (
                    obj.post_rating.get().salary +
                    obj.post_rating.get().team +
                    obj.post_rating.get().education +
                    obj.post_rating.get().management +
                    obj.post_rating.get().social_package +
                    obj.post_rating.get().office_comfort
                   ) / 6    # noqa: JS102
        return avg_rate

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_views_count(self, obj):
        return obj.views.count()

    def get_comments_count(self, obj):
        return obj.post_comment.count()


class PostWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'field_of_activity', 'title',
            'company', 'website', 'location', 'position', 'work_time_from', 'work_time_to', 'body',
            'negative', 'positive', 'ensemble',
        )

    def validate(self, data):
        if data['work_time_from'] > data['work_time_to']:
            raise serializers.ValidationError('Дата начала должна быть раньше даты окончания.')

        return data


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
