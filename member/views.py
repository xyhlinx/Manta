from lib.tags_filter import TagFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from member.models import Tag
from member.serializer import TagSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth.models import Group, User


class TagList(ListAPIView, CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)

    # filter_class = tags_filter

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            tag_obj = serializer.save()
            user_ids = request.data.get('users', [])
            group_id = request.data.get('group', None)
            group_instance = Group.objects.filter(id=group_id)
            user_instances = User.objects.filter(id__in=user_ids)
            tag_obj.users.set(user_instances)
            if group_instance:
                tag_obj.group = group_instance[0]
                tag_obj.save()
            return Response({'id': tag_obj.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)

