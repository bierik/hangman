from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from api.models import Guess
from api.models import Trophy
from django.conf import settings


class ProfileView(APIView):
    def get(self, request, format=None):
        points = Guess.points()
        level = points % settings.ACHIEVEMENT_COST
        trophies_count = Trophy.received().count()
        max_trophies_count = Trophy.objects.all().count()
        return Response(data={
            'level': level,
            'trophies_count': trophies_count,
            'max_trophies_count': max_trophies_count
        })
