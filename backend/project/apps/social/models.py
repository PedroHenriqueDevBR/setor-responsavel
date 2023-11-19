from django.db import models


class SocialAction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    multiplier = models.FloatField()
    done = models.BooleanField(default=False)
