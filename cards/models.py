from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from members.models import Member


class Card(models.Model):

    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    card = models.CharField(
        verbose_name="Card ID",
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return '%s' % self.card
