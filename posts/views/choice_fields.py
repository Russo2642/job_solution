from posts.models import Post
from posts.models.post import FieldOfActivityChoice, EnsembleChoice
from rest_framework.response import Response
from rest_framework.views import APIView


class ActivityViewSet(APIView):
    def get(self, request):
        choices = {choice[0]: choice[1] for choice in FieldOfActivityChoice.choices}
        return Response(choices)


class EnsembleViewSet(APIView):
    def get(self, request):
        choices = {choice[0]: choice[1] for choice in EnsembleChoice.choices}
        return Response(choices)


class PositionViewSet(APIView):
    def get(self, request):
        choices = [choice.position for choice in Post.objects.all()]
        return Response(choices)


class LocationViewSet(APIView):
    def get(self, request):
        choices = [choice.location for choice in Post.objects.all()]
        return Response(choices)
