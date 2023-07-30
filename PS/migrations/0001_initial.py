# Generated by Django 4.2.3 on 2023-07-30 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='firstname')),
                ('surname', models.CharField(max_length=64, null=True, verbose_name='surname')),
                ('number', models.CharField(max_length=12, verbose_name='number')),
                ('email', models.CharField(max_length=64, verbose_name='email')),
                ('telegram_id', models.CharField(max_length=64, null=True, verbose_name='telegram_id')),
                ('orders_count', models.IntegerField(verbose_name='orders_count')),
                ('permissions', models.JSONField(null=True, verbose_name='permissions')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='reg_date')),
            ],
            options={
                'verbose_name': 'basic_user',
                'verbose_name_plural': 'basic_users',
            },
        ),
        migrations.CreateModel(
            name='CompanyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='reg_date')),
                ('order_name', models.CharField(max_length=128, verbose_name='order_name')),
                ('description', models.CharField(max_length=1024, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyOrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=128, null=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'company_order_status_enum',
                'verbose_name_plural': 'company_order_status_enum',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=100, verbose_name='lab_name')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='reg_date')),
                ('order_name', models.CharField(max_length=128, verbose_name='order_name')),
                ('description', models.CharField(max_length=1024, null=True, verbose_name='description')),
                ('deadline', models.DateTimeField(null=True, verbose_name='deadline')),
                ('exec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Имя', to='PS.basicuser')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab')),
            ],
            options={
                'verbose_name': 'order_model',
                'verbose_name_plural': 'order_model',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=128, null=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'order_status_enum',
                'verbose_name_plural': 'order_status_enum',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(max_length=128, null=True, verbose_name='role')),
            ],
            options={
                'verbose_name': 'role_enum',
                'verbose_name_plural': 'role_enum',
            },
        ),
        migrations.CreateModel(
            name='CreateCompanyOrder',
            fields=[
                ('companyorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PS.companyorder')),
            ],
            options={
                'verbose_name': 'order_placed',
                'verbose_name_plural': 'order_placed',
            },
            bases=('PS.companyorder',),
        ),
        migrations.CreateModel(
            name='OrderInProccess',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PS.order')),
            ],
            options={
                'verbose_name': 'order_in_proccess',
                'verbose_name_plural': 'order_in_proccess',
            },
            bases=('PS.order',),
        ),
        migrations.CreateModel(
            name='OrderPaid',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PS.order')),
            ],
            options={
                'verbose_name': 'order_paid',
                'verbose_name_plural': 'order_paid',
            },
            bases=('PS.order',),
        ),
        migrations.CreateModel(
            name='OrderPlace',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PS.order')),
            ],
            options={
                'verbose_name': 'order_place',
                'verbose_name_plural': 'order_place',
            },
            bases=('PS.order',),
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PS.order')),
            ],
            options={
                'verbose_name': 'order_placed',
                'verbose_name_plural': 'order_placed',
            },
            bases=('PS.order',),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Статус', to='PS.orderstatus'),
        ),
        migrations.AddField(
            model_name='companyorder',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PS.lab'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Роль', to='PS.role'),
        ),
    ]
