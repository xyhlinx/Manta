import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from member.models import Tag
from member.serializer import TagDetailSerializer, UserSerializer, GroupSerializer
from rest_framework import status
from django.contrib.auth.models import Group, User


class TagListCreate(ListAPIView, CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    filter_backends = (DjangoFilterBackend,)

    # filter_class = tags_filter

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        serializer = TagDetailSerializer(data=request.data)
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


class TagDetail(RetrieveAPIView, DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer

    def get(self, request, pk):
        tag_instance = self.queryset.filter(id=pk)
        if not tag_instance:
            return Response({'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TagDetailSerializer(tag_instance[0])
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        tag_instance = self.queryset.filter(id=pk)
        if not tag_instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        tag_instance[0].delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        tag_instance = self.queryset.filter(id=pk)
        if not tag_instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        tag_instance = tag_instance[0]
        serializer = TagDetailSerializer(tag_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        if 'users' in request.data:
            user_ids = request.data.get('users', [])
            user_instances = User.objects.filter(id__in=user_ids)
            tag_instance.users.set(user_instances)
        if 'group' in request.data:
            group_id = request.data.get('group', None)
            group_instance = Group.objects.filter(id=group_id)
            if group_instance:
                tag_instance.update(group=group_instance[0])
        return Response({'id': tag_instance.id}, status=status.HTTP_201_CREATED)


class UserList(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, )

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        if username:
            user_instance = User.objects.create_user(username)
            return Response({'id': user_instance.id}, status=status.HTTP_201_CREATED)
        return Response({'error'}, status=status.HTTP_400_BAD_REQUEST)


class GroupList(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend, )

