from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel
from django.db.models import Sum
from django.db.models import Q


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
        CREATED = 'CR', 'Erstellt'

    dictionary = models.ForeignKey(Dictionary, on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.CREATED)

    @classmethod
    def current(cls):
        return cls.objects.filter().order_by('-created').first()

    @classmethod
    def available(cls):
        current_game = timezone.now().replace(hour=7, minute=0, second=0, microsecond=0)
        already_played = cls.objects.filter(Q(status=cls.Status.SUCCESSFUL) | Q(status=cls.Status.FAILED), created__gte=current_game)
        return not already_played.exists()

    @classmethod
    def successful(cls):
        return cls.objects.filter(status=cls.Status.SUCCESSFUL)

    @classmethod
    def points(cls):
        return cls.successful().aggregate(points=Sum('dictionary__length')).get('points', 0) or 0

    @classmethod
    def random(cls):
        previous_game = timezone.now().replace(hour=7, minute=0, second=0, microsecond=0)
        cls.objects.filter(Q(status=cls.Status.RUNNING) | Q(status=cls.Status.CREATED), created__lte=previous_game).update(status=cls.Status.FAILED)
        maybe_running = cls.objects.filter(Q(status=cls.Status.RUNNING) | Q(status=cls.Status.CREATED), created__gte=previous_game)
        if maybe_running.exists():
            return maybe_running.first()
        return Guess.objects.create(dictionary=Dictionary.random())

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

    def start(self):
        if self.status != self.Status.CREATED:
            return
        self.status = self.Status.RUNNING
        self.save()

    def stop(self):
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
    expandable = models.BooleanField(verbose_name="Vergrösserbar", default=False)

    def __str__(self):
        return f"{self.title}, {self.subtitle}"

    def receive(self):
        self.received_at = timezone.now()
        self.save()

    @classmethod
    def received(cls):
        now = timezone.now()
        return cls.objects.filter(received_at__lte=now)

    @classmethod
    def receiveRandom(cls):
        open = cls.objects.filter(received_at__isnull=True)
        to_receive = open.order_by('?').first()
        if to_receive is not None:
            to_receive.receive()
            to_receive.refresh_from_db()
            return to_receive
        return None

    def consume(self):
        if self.consumed_at is not None:
            return
        self.consumed_at = timezone.now()
        self.save()
