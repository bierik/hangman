from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Guess
from api.models import Trophy
from api.models import Config


class ProfileView(APIView):
    def get(self, request, format=None):
        points = Guess.points()
        level = points % Config.default('ACHIEVEMENT_COST')
        trophies_count = Trophy.received().count()
        max_trophies_count = Trophy.objects.all().count()
        return Response(data={
            'level': level,
            'trophies_count': trophies_count,
            'max_trophies_count': max_trophies_count
        })


class ConfigView(APIView):
    def get(self, request, format=None):
        return Response(data={
            'achievementCost': Config.default('ACHIEVEMENT_COST'),
            'timerInterval': Config.default('TIMER_INTERVAL'),
        })
