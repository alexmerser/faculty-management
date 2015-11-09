from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name