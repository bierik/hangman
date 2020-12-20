from rest_framework.serializers import Serializer
from rest_framework import fields
from api.models import Guess

class GuessSerializer(Serializer):
    word = fields.CharField()

    class Meta:
        model = Guess
