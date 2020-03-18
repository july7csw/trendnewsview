from django.conf import settings
from django.db import models
from django.utils import timezone



class News(models.Model):
    pubdate = models.DateTimeField(
            blank=True, null=True)
    title = models.CharField(max_length=1000)
    media = models.CharField(max_length=20)
    summary = models.TextField()
    link = models.TextField()
    category = models.CharField(max_length=20)
    period = models.CharField(max_length=20)

    def __str__(self):
        return self.title



