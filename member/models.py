import uuid
from django.db import models
from django.contrib.auth.models import User, Group


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    user = models.ManyToManyField(User, related_name='user_tags', blank=True)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='group_tags', null=True, blank=True)
