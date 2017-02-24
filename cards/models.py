from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from members.models import Member


class Card(models.Model):

    member = models.ForeignKey(Member)

    card = models.TextField(
        verbose_name="Card ID",
    )

