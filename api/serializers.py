from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import Guess
from api.models import Dictionary
from api.models import Trophy
from django.utils import timezone


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'word', 'length')


class GuessSerializer(ModelSerializer):
    dictionary = DictionarySerializer()

    class Meta:
        model = Guess
        fields = ('id', 'status', 'dictionary', 'created')


class TrophySerializer(ModelSerializer):
    file = serializers.SerializerMethodField()
    is_consumed = serializers.SerializerMethodField()

    class Meta:
        model = Trophy
        fields = ('id', 'title', 'subtitle', 'consumable', 'consumed_at', 'file', 'link', 'is_consumed')

    def get_file(self, obj):
        if obj.file and hasattr(obj.file, 'url'):
            return obj.file.url
        return None

    def get_is_consumed(self, obj):
        now = timezone.now()
        if obj.consumed_at is None:
            return False
        return obj.consumed_at < now
