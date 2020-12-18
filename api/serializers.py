from django.db import models
from rest_framework.serializers import Serializer
from rest_framework import fields
from api.models import GuessText

class GuessTextSerializer(Serializer):
    text = fields.CharField()
    length = fields.IntegerField()

    class Meta:
        model = GuessText
