from django.db import models
from rspades import build
import json


class Deck(models.Model):
    cards = models.CharField(max_length=500)

