from django.db import models
from uuid import uuid4


class Escola(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100, null=False, blank=False)

class Classe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    serie = models.IntegerField(null=False, blank=False)
    turma = models.CharField(max_length=1, null=False, blank=False)