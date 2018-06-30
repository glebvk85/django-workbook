from django.db import models
from django.utils import timezone


class Notification(models.Model):
    title = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
