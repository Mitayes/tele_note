from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую просматривает пользователь."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    tags = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_saved = models.DateTimeField(auto_now_add=True)
    # task_type =

    def __str__(self):
        return self.header
