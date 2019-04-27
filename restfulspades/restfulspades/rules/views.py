from django.http import HttpResponse, JsonResponse
from rules.models import Ruleset
from rules.serializers import RulesetSerializer
from rest_framework import generics


class RuleList(generics.ListCreateAPIView):
    queryset = Ruleset.objects.all()
    serializer_class = RulesetSerializer

