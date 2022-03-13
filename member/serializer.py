from django.contrib.auth.models import User, Group
from rest_framework import serializers
from member.models import Tag


class TagSerializer(serializers.Serializer):
    name = serializers.StringRelatedField(many=False, read_only=True)
    id = serializers.StringRelatedField(many=False, read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    group = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    tag = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'tag')

