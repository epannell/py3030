from rest_framework import serializers
from rules.models import Ruleset


class RulesetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruleset
        fields = ('rules',)
