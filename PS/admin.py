from django.contrib import admin
from PS import models


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lab)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BasicUser)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderStatus)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderPaid)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderInProccess)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderPlace)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderPlaced)
class UsersAdmin(admin.ModelAdmin):
    pass
