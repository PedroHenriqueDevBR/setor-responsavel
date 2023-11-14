from django.db import models
from django.contrib.auth.models import User


class Subsidiary(models.Model):
    name = models.CharField(max_length=250)


class Sector(models.Model):
    name = models.CharField(max_length=250)
    subsidiary = models.ForeignKey(
        Subsidiary,
        on_delete=models.SET_NULL,
        related_name="sectors",
        null=True,
        blank=True,
    )


class Employee(models.Model):
    contact = models.CharField(max_length=150)
    identifier = models.CharField(max_length=150)
    sector = models.OneToOneField(
        Sector,
        on_delete=models.SET_NULL,
        related_name="employeers",
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name="employee",
        null=True,
        blank=True,
    )
