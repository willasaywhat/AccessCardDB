from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Member(models.Model):

    name = models.CharField(
        verbose_name="Member Name",
        max_length=255,
        unique=True,
    )

    notes = models.TextField(
        verbose_name="Notes",
        blank=True,
        null=True,
    )

    STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Inactive'),
    )

    status = models.IntegerField(
        verbose_name="Status",
        choices=STATUS_CHOICES,
    )

    def __str__(self):
        return '%s' % self.name