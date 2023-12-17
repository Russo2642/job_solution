from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostWriteSerializer, PostReadSerializer
from rest_framework import viewsets, filters, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']

    filterset_fields = ['title', 'location', 'position', 'author', 'field_of_activity']
    ordering_fields = ['created_at']

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return PostWriteSerializer

        return PostReadSerializer

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()


class LikePostAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        data = {}

        if user in post.likes.all():
            post.likes.remove(user)
            data = {'message': f'{user.email} delete'}

        else:
            post.likes.add(user)
            data = {'message': f'{user.email} added '}

        return Response(status=status.HTTP_200_OK, data=data)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        likes = [like.email for like in post.likes.all()]
        return Response(status=status.HTTP_200_OK, data=likes)


class ViewsPostAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)

        if user not in post.views.all():
            post.views.add(user)

        return Response(status=status.HTTP_200_OK, data={'message': f'{user.email} added '})

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        views = [view.email for view in post.views.all()]
        return Response(status=status.HTTP_200_OK, data=views)
