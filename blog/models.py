from django.db import models
# from django.contrib.auth.models import User 비추
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.
    title = models.CharField(max_length=144)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.author, self.title)
