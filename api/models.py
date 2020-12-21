from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel


class Dictionary(models.Model):
    word = models.TextField(verbose_name="Wort")
    length = models.IntegerField(verbose_name="Länge")

    @classmethod
    def random(cls):
        return cls.objects.order_by('?').first()

class Guess(TimeStampedModel):
    class Status(models.TextChoices):
        SUCCESSFUL = 'SU', 'Geglückt'
        FAILED = 'FA', 'Gescheitert'
        RUNNING = 'RU', 'Läuft'

    dictionary = models.ForeignKey(Dictionary, on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.RUNNING)

    @classmethod
    def current(cls):
        return cls.objects.order_by('-created').first()

    @classmethod
    def available(cls):
        next_game = timezone.now().replace(hour=7, minute=0, second=0, microsecond=0)
        if cls.current() is None:
            return True
        return cls.current().created < next_game

    @classmethod
    def successful(cls):
        return cls.objects.filter(status=cls.Status.SUCCESSFUL)

    def success(self):
        if self.status != self.Status.RUNNING:
            return
        self.status = self.Status.SUCCESSFUL
        self.save()

    def fail(self):
        if self.status != self.Status.RUNNING:
            return
        self.status = self.Status.FAILED
        self.save()

class Trophy(models.Model):
    received_at = models.DateTimeField(verbose_name="Erhalten am", blank=True, null=True)
    title = models.TextField(verbose_name="Titel")
    subtitle = models.TextField(verbose_name="Untertitel")
    consumable = models.BooleanField(verbose_name="Verbrauchbar")
    consumed_at = models.DateTimeField(verbose_name="Verbraucht am", blank=True, null=True)
    link = models.URLField(verbose_name="Link", blank=True, null=True)
    file = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.subtitle}"

    def consume(self):
        if self.consumed_at is not None:
            return
        self.consumed_at = timezone.now()
        self.save()
