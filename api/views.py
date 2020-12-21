from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from api.models import Guess
from django.conf import settings


class ProfileView(APIView):
    def get(self, request, format=None):
        points = Guess.successful().aggregate(points=Sum('dictionary__length')).get('points', 0) or 0
        level = points % settings.ACHIEVEMENT_COST
        return Response(data={ 'level': level })
