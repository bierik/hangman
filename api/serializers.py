from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from api.models import Guess
from api.models import Dictionary


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'word', 'length')


class GuessSerializer(ModelSerializer):
    dictionary = DictionarySerializer()

    class Meta:
        model = Guess
        fields = ('id', 'status', 'dictionary')
