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


class UserDetailSerializer(serializers.ModelSerializer):
    """Пользователь"""

    lab = serializers.SlugRelatedField(slug_field='lab_name', queryset=Lab.objects.all())
    role = serializers.SlugRelatedField(slug_field='role_name', queryset=Role.objects.all())

    class Meta:
        model = BasicUser
        # exclude = ('password, ')
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = BasicUser
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    """Новый пользователь"""

    class Meta:
        model = BasicUser
        fields = ('username', 'password', 'lab', 'role')
        extra_kwargs = {
            'lab': {'required': True},
            'role': {'required': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data.pop['username']
        password = validated_data.pop('password')
        lab = validated_data.pop('lab')
        role = validated_data.pop('role')

        # временное решение
        user = BasicUser.objects.create_user(username=username, password=password, lab=lab, role=role)

        return user


# возможно избыточный
class UserUpdateSerializer(serializers.ModelSerializer):
    """Обновить пользователя"""

    class Meta:
        model = BasicUser
        fields = "__all__"


class ScheduleDetailSerializer(serializers.ModelSerializer):
    """Расписание"""

    lab = serializers.SlugRelatedField(slug_field='lab_name', queryset=Lab.objects.all())
    employee = serializers.SlugRelatedField(slug_field='last_name', queryset=BasicUser.objects.all())

    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleListSerializer(serializers.ModelSerializer):
    """Список дней"""

    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleCreateSerializer(serializers.ModelSerializer):
    """Новое расписание"""

    class Meta:
        model = Schedule
        fields = "__all__"
        extra_kwargs = {
            'lab': {'required': True},
            'role': {'required': True},
            'date': {'required': True}
        }


# возможно избыточный
class ScheduleUpdateSerializer(serializers.ModelSerializer):
    """Обновить расписание"""

    class Meta:
        model = Schedule
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    """Заказ"""

    lab = serializers.SlugRelatedField(slug_field='lab_name', queryset=Lab.objects.all())
    exec = serializers.SlugRelatedField(slug_field='last_name', queryset=BasicUser.objects.all())

    class Meta:
        model = Order
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):
    """Список заказов"""

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    """Новый заказ"""

    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            'lab': {'required': True},
            'order_creator': {'required': True}
        }

    # def create(self, request):
    #     exec = request.get('exec')
    #     if exec:
    #         if exec.orders_count:
    #             exec.orders_count += 1
    #         else:
    #             exec.orders_count = 1


# возможно избыточный
class OrderUpdateSerializer(serializers.ModelSerializer):
    """Обновить заказ"""

    class Meta:
        model = Order
        fields = "__all__"


class CompanyOrderDetailSerializer(serializers.ModelSerializer):
    """Заказ"""

    lab = serializers.SlugRelatedField(slug_field='lab_name', queryset=Lab.objects.all())
    exec = serializers.SlugRelatedField(slug_field='last_name', queryset=BasicUser.objects.all())

    class Meta:
        model = CompanyOrder
        fields = "__all__"


class CompanyOrderListSerializer(serializers.ModelSerializer):
    """Список заказов"""

    class Meta:
        model = CompanyOrder
        fields = "__all__"


class CompanyOrderCreateSerializer(serializers.ModelSerializer):
    """Новый заказ"""

    class Meta:
        model = CompanyOrder
        fields = "__all__"
        extra_kwargs = {
            'lab': {'required': True},
            'order_creator': {'required': True}
        }


class CompanyOrderUpdateSerializer(serializers.ModelSerializer):
    """Обновить заказ"""

    class Meta:
        model = CompanyOrder
        fields = "__all__"


class NewsDetailSerializer(serializers.ModelSerializer):
    """Новость"""

    class Meta:
        model = News
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    """Список новостей"""

    class Meta:
        model = News
        fields = "__all__"


class NewsCreateSerializer(serializers.ModelSerializer):
    """Новая новость"""

    class Meta:
        model = News
        fields = "__all__"
        extra_kwargs = {
            'news_type': {'required': True},
            'editor': {'required': True}
        }


class NewsUpdateSerializer(serializers.ModelSerializer):
    """Обновить новость"""

    class Meta:
        model = News
        fields = "__all__"
