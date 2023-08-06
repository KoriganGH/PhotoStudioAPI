from rest_framework import serializers
from .models import *


class LabDetailSerializer(serializers.ModelSerializer):
    """Лаборатория"""

    class Meta:
        model = Lab
        fields = "__all__"


class RoleDetailSerializer(serializers.ModelSerializer):
    """Роль"""

    class Meta:
        model = Role
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = BasicUser
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    """Пользователь"""

    lab = serializers.SlugRelatedField(slug_field='lab_name', queryset=Lab.objects.all())
    role = serializers.SlugRelatedField(slug_field='role_name', queryset=Role.objects.all())

    class Meta:
        model = BasicUser
        # exclude = ('password, ')
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    """Новый пользователь"""

    class Meta:
        model = BasicUser
        fields = "__all__"
        extra_kwargs = {
            'lab': {'required': True},
            'role': {'required': True},
            'password': {'write_only': True}
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    """Обновить пользователя"""

    class Meta:
        model = BasicUser
        fields = "__all__"


class UserLabListSerializer(UserListSerializer):
    extra_kwargs = {
        'date': {'required': True},
        'lab': {'required': True},
    }




