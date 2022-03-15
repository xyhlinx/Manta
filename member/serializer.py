from django.contrib.auth.models import User, Group
from rest_framework import serializers
from member.models import Tag


class TagListSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Tag
        fields = ('id', 'name', )


class UserSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    username = serializers.StringRelatedField(many=False, read_only=True)
    user_tags = TagListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_tags', 'username')


class GroupSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    name = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Group
        fields = ('id', )


class TagDetailSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    name = serializers.CharField(max_length=200)
    users = UserSerializer(many=True, read_only=True)
    group = GroupSerializer(many=False, read_only=True)

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Tag
        fields = ('name', 'users', 'group', 'id')
