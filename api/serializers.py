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
    image = serializers.SerializerMethodField()
    preview = serializers.SerializerMethodField()
    is_consumed = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()

    class Meta:
        model = Trophy
        fields = ('id', 'title', 'subtitle', 'consumable', 'consumed_at', 'image', 'preview', 'link', 'is_consumed', 'expandable', 'width', 'height')

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        return None

    def get_preview(self, obj):
        if obj.image:
            return obj.image['preview'].url
        return None

    def get_is_consumed(self, obj):
        now = timezone.now()
        if obj.consumed_at is None:
            return False
        return obj.consumed_at < now

    def get_width(self, obj):
        if obj.image:
            return obj.image.width
        return None

    def get_height(self, obj):
        if obj.image:
            return obj.image.height
        return None
