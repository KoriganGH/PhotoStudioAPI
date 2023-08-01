from django.contrib import admin
from PS import models


@admin.register(models.Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ['lab_name']


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']


@admin.register(models.BasicUser)
class UsersAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('User Information', {
    #         'fields': ('first_name', 'last_name'),
    #     }),)
    list_display = ['id', 'first_name', 'last_name', 'number', 'email', 'orders_count']
    #list_display = ['id', 'first_name', 'surname', 'number', 'email', 'role', 'lab', 'orders_count']


@admin.register(models.OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_name', 'status', 'exec', 'order_creator', 'deadline']


@admin.register(models.CompanyOrderStatus)
class CompanyOrderStatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']


@admin.register(models.CompanyOrder)
class CompanyOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_name', 'status', 'exec', 'order_creator', 'deadline']


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'lab', 'employee', 'date']


@admin.register(models.NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'content', 'editor', 'news_type']


