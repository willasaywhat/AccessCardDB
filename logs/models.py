from __future__ import unicode_literals

from django.db import models
from cards.models import Card
from members.models import Member


# Create your models here.
class Log(models.Model):
    card_scanned = models.CharField(
        verbose_name="Card ID Scanned",
        max_length=255,
    )

    member_name = models.CharField(
        verbose_name="Member Name",
        max_length=255,
        blank=True,
        null=True,
    )

    STATUS_CHOICES = (
        (1, 'Granted'),
        (0, 'Denied'),
    )

    status_at_scan = models.IntegerField(
        verbose_name="Status",
        choices=STATUS_CHOICES,
    )

    scanned_at = models.DateTimeField(auto_now_add=True, verbose_name="Time Scanned")
