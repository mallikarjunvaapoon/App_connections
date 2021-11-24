from django.db import models
from ..User.models import User

class Status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status

class Sender(models.Model):
    name = models.CharField(max_length=20)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

class Receiver(models.Model):
    name = models.CharField(max_length=20)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

