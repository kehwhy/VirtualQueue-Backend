import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=100, blank=True, unique=True, default=uuid.uuid4)
    username = models.CharField(max_length=60, unique=True,null=True)
    name = models.CharField(max_length=60, default="")
    email = models.CharField(max_length=60, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.name)

class Line(models.Model):
    id = models.CharField(primary_key=True, max_length=100, blank=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=60, default="")
    timestamp = models.DateTimeField(default=timezone.now)
    manager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    customers = models.ManyToManyField(User, related_name='customers')

    def __str__(self):
        return str(self.name)
