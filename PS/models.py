from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Model, CASCADE, DateField
from django.db.models import CharField, ForeignKey, IntegerField, JSONField, DateTimeField, BooleanField, BinaryField
from django.contrib.auth.models import AbstractUser


class Lab(Model):
    lab_name = CharField("lab_name", max_length=100, null=False)

    def __str__(self):
        return self.lab_name

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'


class Role(Model):
    role_name = CharField("role", max_length=128, null=True)

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, lab, role, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not lab:
            raise ValueError('The Lab field must be set')
        if not role:
            raise ValueError('The Role field must be set')

        user = self.model(username=username, lab=lab, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, lab, role, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, lab, role, **extra_fields)


class BasicUser(AbstractUser):
    first_name = CharField(max_length=64, null=False)
    number = CharField(max_length=12, null=False)
    email = CharField(max_length=64, null=False)
    role = ForeignKey(Role, on_delete=CASCADE)
    lab = ForeignKey(Lab, on_delete=CASCADE)
    telegram_id = CharField(max_length=64, null=True)
    orders_count = IntegerField(null=True)
    permissions = JSONField(null=True)
    availableToday = BooleanField(null=True)
    registration_date = DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class OrderStatus(Model):
    status_name = CharField(max_length=128, null=True)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(Model):
    creation_date = DateTimeField(auto_now_add=True)
    lab = ForeignKey(Lab, on_delete=CASCADE)
    order_name = CharField(max_length=128, null=False)
    description = CharField(max_length=1024, null=True)
    status = ForeignKey(OrderStatus, on_delete=CASCADE)
    exec = ForeignKey(BasicUser, on_delete=CASCADE, null=True, related_name='exec_of')
    order_creator = ForeignKey(BasicUser, on_delete=CASCADE, related_name='orders_created_by')
    deadline = DateTimeField(null=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CompanyOrderStatus(Model):
    status_name = CharField("status", max_length=128, null=True)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус заказа компании'
        verbose_name_plural = 'Статусы заказов компании'


class CompanyOrder(Model):
    creation_date = DateTimeField(auto_now_add=True)
    lab = ForeignKey(Lab, on_delete=CASCADE)
    order_name = CharField(max_length=128, null=False)
    description = CharField(max_length=1024, null=True)
    status = ForeignKey(CompanyOrderStatus, on_delete=CASCADE)
    exec = ForeignKey(BasicUser, on_delete=CASCADE, null=True, related_name='company_exec_of')
    order_creator = ForeignKey(BasicUser, on_delete=CASCADE, related_name='company_orders_created_by')
    deadline = DateTimeField(null=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ компании'
        verbose_name_plural = 'Заказы компании'


class Schedule(Model):
    date = DateField()
    employee = ForeignKey(BasicUser, on_delete=CASCADE, related_name='days')
    lab = ForeignKey(Lab, on_delete=CASCADE)

    # def __str__(self):
    #     return self.employee

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class NewsType(Model):
    type = CharField(max_length=128, null=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип новости'
        verbose_name_plural = 'Типы новостей'


class News(Model):
    news_type = ForeignKey(NewsType, on_delete=CASCADE)
    header = CharField(max_length=256, null=False)
    picture = BinaryField(null=True)
    content = CharField(max_length=1028, null=False)
    telegram_post = BooleanField(null=True, default=False)
    post_date = DateTimeField(auto_now_add=True)
    editor = ForeignKey(BasicUser, on_delete=CASCADE)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
