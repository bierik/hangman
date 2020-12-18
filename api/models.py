from django.db import models
from django.db.models import fields


class GuessText(models.Model):
    text = fields.TextField(verbose_name="Text")
    length = fields.IntegerField(verbose_name="Länge")
