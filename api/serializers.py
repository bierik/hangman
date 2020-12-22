from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import Guess
from api.models import Dictionary
from api.models import Trophy
from django.utils import timezone
from django.core.files.images import get_image_dimensions


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
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()

    class Meta:
        model = Trophy
        fields = ('id', 'title', 'subtitle', 'consumable', 'consumed_at', 'file', 'link', 'is_consumed', 'width', 'height', 'expandable')

    def get_file(self, obj):
        if obj.file and hasattr(obj.file, 'url'):
            return obj.file.url
        return None

    def get_is_consumed(self, obj):
        now = timezone.now()
        if obj.consumed_at is None:
            return False
        return obj.consumed_at < now

    def get_width(self, obj):
        width, _ = get_image_dimensions(obj.file)
        return width

    def get_height(self, obj):
        _, height = get_image_dimensions(obj.file)
        return height
