from django.db import models
from apps.users.models import Sector
from apps.social.models import SocialAction


class Scores(models.Model):
    INCREASE = 0
    DECREASE = 1
    SCORE_TYPE = [
        ("Increase", 0),
        ("Decrease", 1),
    ]

    name = models.CharField(max_length=250)
    quantity = models.IntegerField(default=0)
    identifier = models.IntegerField(choices=SCORE_TYPE)


class Ranking(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    initial_date = models.DateField()
    final_date = models.DateField()
    done = models.BooleanField(default=False)
    social = models.OneToOneField(
        SocialAction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rankig",
    )


class Action(models.Model):
    action_date = models.DateTimeField(auto_now_add=True)
    ranking = models.ForeignKey(
        Ranking,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ranking_actions",
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sector_actions",
    )
    score = models.ForeignKey(
        Scores,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="score_actions",
    )


class Award(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
