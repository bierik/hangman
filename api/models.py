from django.db import models
from django.db.models import fields
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel


class Dictionary(models.Model):
    word = fields.TextField(verbose_name="Wort")
    length = fields.IntegerField(verbose_name="Länge")

    @classmethod
    def random(cls):
        return cls.objects.order_by('?').first()

class Guess(TimeStampedModel):
    class Status(models.TextChoices):
        SUCCESSFUL = 'SU', 'Geglückt'
        FAILED = 'FA', 'Gescheitert'
        RUNNING = 'RU', 'Läuft'

    dictionary = models.ForeignKey(Dictionary, on_delete=models.PROTECT)
    status = fields.CharField(max_length=2, choices=Status.choices, default=Status.RUNNING)

    @classmethod
    def current(cls):
        return cls.objects.order_by('-created').first()

    @classmethod
    def available(cls):
        next_game = timezone.now().replace(hour=7, minute=0, second=0, microsecond=0)
        if cls.current() is None:
            return True
        return cls.current().created < next_game

    def success(self):
        self.status = self.Status.SUCCESSFUL
        self.save()

    def fail(self):
        self.status = self.Status.FAILED
        self.save()
