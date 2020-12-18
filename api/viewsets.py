from rest_framework import viewsets
from rest_framework.response import Response
from api.models import GuessText
from api.serializers import GuessTextSerializer
from rest_framework.decorators import action

class GuessTextViewSet(viewsets.GenericViewSet):
    queryset = GuessText.objects.all()
    serializer_class = GuessTextSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        return Response(GuessTextSerializer(GuessText.objects.order_by('?').first()).data)
