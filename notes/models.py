from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
