from rest_framework import permissions, viewsets

from posts.models import Rating
from posts.serializers import RatingReadSerializer


class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingReadSerializer
    permission_classes = (permissions.AllowAny,)
