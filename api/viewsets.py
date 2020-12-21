from rest_framework import status, viewsets
from rest_framework.response import Response
from api.models import Dictionary
from api.models import Guess
from api.models import Trophy
from api.serializers import GuessSerializer
from api.serializers import TrophySerializer
from rest_framework.decorators import action
from django.utils import timezone

class GuessViewSet(viewsets.GenericViewSet):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        if not Guess.available():
            return Response(
                data={ 'code': 'NO_GUESS_AVAILABLE', 'message': 'Es ist heute kein Versuch mehr möglich.' }, status=status.HTTP_400_BAD_REQUEST
            )
        guess = Guess.objects.create(dictionary=Dictionary.random())
        return Response(GuessSerializer(guess).data)

    @action(detail=True, methods=['post'])
    def success(self, request, pk=None):
        guess = self.get_object()
        guess.success()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def fail(self, request, pk=None):
        guess = self.get_object()
        guess.fail()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrophyViewSet(viewsets.ModelViewSet):
    queryset = Trophy.objects.all().order_by('-received_at')
    serializer_class = TrophySerializer

    def list(self, request, *args, **kwargs):
        now = timezone.now()
        return Response(self.get_serializer(self.get_queryset().filter(received_at__lte=now), many=True).data)

    @action(detail=True, methods=['post'])
    def consume(self, request, pk=None):
        trophy = self.get_object()
        trophy.consume()
        trophy.refresh_from_db()
        return Response(self.get_serializer(trophy).data)
