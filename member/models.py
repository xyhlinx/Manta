import uuid
from django.db import models
from django.contrib.auth.models import User, Group


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    users = models.ManyToManyField(User, related_name='user_tags', blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='group_tags', null=True, blank=True)
