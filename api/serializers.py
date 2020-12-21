from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import Guess
from api.models import Dictionary
from api.models import Trophy


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'word', 'length')


class GuessSerializer(ModelSerializer):
    dictionary = DictionarySerializer()

    class Meta:
        model = Guess
        fields = ('id', 'status', 'dictionary')


class TrophySerializer(ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Trophy
        fields = ('id', 'title', 'subtitle', 'consumable', 'consumed_at', 'file', 'link')

    def get_file(self, obj):
        return obj.file.url
