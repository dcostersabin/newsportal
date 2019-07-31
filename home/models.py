from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Interest(models.Model):
    category = models.TextField()
    sources = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
