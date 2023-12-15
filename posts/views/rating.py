from rest_framework import permissions, viewsets

from posts.models import Rating
from posts.serializers import RatingReadSerializer, RatingWriteSerializer

from posts.permissions import IsAuthorOrReadOnly

# class RatingViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingReadSerializer
#     permission_classes = (permissions.AllowAny,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingReadSerializer
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return RatingWriteSerializer

        return RatingReadSerializer

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()
