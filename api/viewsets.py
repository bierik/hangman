from rest_framework import status, viewsets
from rest_framework.response import Response
from api.models import Guess
from api.models import Trophy
from api.serializers import GuessSerializer
from api.serializers import TrophySerializer
from rest_framework.decorators import action
from django.conf import settings

class GuessViewSet(viewsets.ModelViewSet):
    queryset = Guess.objects.all().order_by('-created')
    serializer_class = GuessSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        if not Guess.available():
            return Response(
                data={ 'code': 'NO_GUESS_AVAILABLE', 'message': 'Es ist heute kein Versuch mehr möglich.' }, status=status.HTTP_400_BAD_REQUEST
            )
        guess = Guess.random()
        return Response(GuessSerializer(guess).data)

    @action(detail=True, methods=['post'])
    def success(self, request, pk=None):
        guess = self.get_object()
        guess.success()
        if Guess.points() >= settings.ACHIEVEMENT_COST:
            received_trophy = Trophy.receiveRandom()
            if received_trophy is not None:
                return Response({ 'received': TrophySerializer(received_trophy).data })
        return Response({ 'received': None })

    @action(detail=True, methods=['post'])
    def fail(self, request, pk=None):
        guess = self.get_object()
        guess.fail()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        guess = self.get_object()
        guess.start()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        guess = self.get_object()
        guess.stop()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrophyViewSet(viewsets.ModelViewSet):
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer

    def list(self, request, *args, **kwargs):
        return Response(self.get_serializer(Trophy.received().order_by('-received_at'), many=True).data)

    @action(detail=True, methods=['post'])
    def consume(self, request, pk=None):
        trophy = self.get_object()
        trophy.consume()
        trophy.refresh_from_db()
        return Response(self.get_serializer(trophy).data)
