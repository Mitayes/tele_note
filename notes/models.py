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
        # return self.header
        return '%s %s' % (self.owner, self.header)

    def get_fields(self):
        fields = {
            'header': self.header,
            'tags': self.tags,
            'text': self.text,
            'date_added': self.date_added.strftime("%d-%m-%Y %H:%M"),
            'date_last_saved': self.date_last_saved.strftime("%d-%m-%Y %H:%M"),
        }
        return fields


