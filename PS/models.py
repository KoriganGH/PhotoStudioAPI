from django.db.models import Model, CASCADE
from django.db.models import CharField, ForeignKey, IntegerField, JSONField, DateTimeField
from enum import Enum
from django.contrib.auth.models import AbstractUser


class Lab(Model):
    lab_name = CharField("lab_name", max_length=100, null=False)


class Role(Model):
    role_name = CharField("role", max_length=128, null=True)

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'role_enum'
        verbose_name_plural = 'role_enum'


class BasicUser(Model):
    first_name = CharField("firstname", max_length=64, null=False)
    surname = CharField("surname", max_length=64, null=True)
    number = CharField("number", max_length=12, null=False)
    email = CharField("email", max_length=64, null=False)
    role = ForeignKey(Role, on_delete=CASCADE)
    lab = ForeignKey(Lab, on_delete=CASCADE)
    telegram_id = CharField("telegram_id", max_length=64, null=True)
    orders_count = IntegerField("orders_count", null=False)
    permissions = JSONField("permissions", null=True)
    registration_date = DateTimeField("reg_date", auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.surname)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class OrderStatus(Model):
    status_name = CharField("status", max_length=128, null=True)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(Model):
    creation_date = DateTimeField("reg_date", auto_now_add=True)
    lab = ForeignKey(Lab, on_delete=CASCADE)
    order_name = CharField('order_name', max_length=128, null=False)
    description = CharField('description', max_length=1024, null=True)
    #customer = CharField('')
    exec = ForeignKey(BasicUser, on_delete=CASCADE)
    status = ForeignKey(OrderStatus, on_delete=CASCADE)
    deadline = DateTimeField('deadline', null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderPaid(Order):

    def __str__(self):
        return self.status, self.order_name

    class Meta:
        verbose_name = 'Оплаченный заказ'
        verbose_name_plural = 'Оплаченные заказы'


class OrderInProccess(Order):
    def __str__(self):
        return self.status, self.order_name

    class Meta:
        verbose_name = 'Заказ в работе'
        verbose_name_plural = 'Заказы в работе'


class OrderPlace(Order):
    def __str__(self):
        return self.status, self.order_name

    class Meta:
        verbose_name = 'order_place'
        verbose_name_plural = 'order_place'


class OrderPlaced(Order):
    def __str__(self):
        return self.status, self.order_name

    class Meta:
        verbose_name = 'order_placed'
        verbose_name_plural = 'order_placed'


class CompanyOrderStatus(Model):
    status_name = CharField("status", max_length=128, null=True)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'company_order_status_enum'
        verbose_name_plural = 'company_order_status_enum'


class CompanyOrder(Model):
    creation_date = DateTimeField("reg_date", auto_now_add=True)
    order_name = CharField('order_name', max_length=128, null=False)
    description = CharField('description', max_length=1024, null=True)
    lab = ForeignKey(Lab, on_delete=CASCADE)


class CreateCompanyOrder(CompanyOrder):
    class Meta:
        verbose_name = 'order_placed'
        verbose_name_plural = 'order_placed'

class CompanyOrderProccess(CompanyOrder):
    class Meta:
        verbose_name = 'order_placed'
        verbose_name_plural = 'order_placed'

class CompanyOrderComplete(CompanyOrder):
    class Meta:
        verbose_name = 'order_placed'
        verbose_name_plural = 'order_placed'
