# about/models.py
from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
