from rest_framework import serializers
from .models import User, Profile, Task


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, max_length=128)
    last_name = serializers.CharField(required=True, max_length=128)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)

        user.set_password(password)
        return user


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone', 'photo']


class TaskSerializer(serializers.ModelSerializer):
    user = UserTaskSerializer()

    class Meta:
        model = Task
        fields = ['user', 'title', 'note', 'file', 'created', 'deadline']
