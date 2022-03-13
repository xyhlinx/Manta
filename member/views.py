from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from member.models import Tag
from member.serializer import TagSerializer
from django.contrib.auth.models import Group


class MemberList(APIView, mixins.RetrieveModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    # def delete(self, request, format=None):


class GroupList(APIView):
    queryset = Group.objects.all()

    def get(self, request, format=None):
        return

