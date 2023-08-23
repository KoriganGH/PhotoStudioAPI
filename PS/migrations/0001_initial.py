# Generated by Django 4.2.3 on 2023-08-23 12:50

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyOrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=128, null=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Статус заказа компании',
                'verbose_name_plural': 'Статусы заказов компании',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=100, verbose_name='lab_name')),
            ],
            options={
                'verbose_name': 'Лаборатория',
                'verbose_name_plural': 'Лаборатории',
            },
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Тип новости',
                'verbose_name_plural': 'Типы новостей',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=128, null=True, verbose_name='role')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=64)),
                ('number', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=64)),
                ('telegram_id', models.CharField(max_length=64, null=True)),
                ('orders_count', models.IntegerField(null=True)),
                ('permissions', models.JSONField(null=True)),
                ('availableToday', models.BooleanField(null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to=settings.AUTH_USER_MODEL)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024, null=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('exec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exec_of', to=settings.AUTH_USER_MODEL)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab')),
                ('order_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_created_by', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.orderstatus')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=256)),
                ('picture', models.BinaryField(null=True)),
                ('content', models.CharField(max_length=1028)),
                ('telegram_post', models.BooleanField(default=False, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('news_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.newstype')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='CompanyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024, null=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('exec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_exec_of', to=settings.AUTH_USER_MODEL)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab')),
                ('order_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_orders_created_by', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.companyorderstatus')),
            ],
            options={
                'verbose_name': 'Заказ компании',
                'verbose_name_plural': 'Заказы компании',
            },
        ),
    ]
