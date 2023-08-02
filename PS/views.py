from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from PS.models import BasicUser, Role, Lab, Schedule, Order, OrderStatus, CompanyOrder, CompanyOrderStatus, News, \
    NewsType
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UpdateUserForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, \
    HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from .models import BasicUser, Role, Lab
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'action': openapi.Schema(type=openapi.TYPE_STRING,
                                         description='Action to perform. (add, delete, update, get_all, get_user)'),
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                'number': openapi.Schema(type=openapi.TYPE_STRING, description='Number'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role name'),
                'lab': openapi.Schema(type=openapi.TYPE_INTEGER, description='Lab ID'),
                'telegram_id': openapi.Schema(type=openapi.TYPE_STRING, description='Telegram ID'),
                'orders_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='Orders count'),
                'permissions': openapi.Schema(type=openapi.TYPE_STRING, description='Permissions'),
            }
        )
    )
    def post(self, request):
        action = request.data.get('action')
        if action == 'add':
            return self.add_new_user(request)
        elif action == 'delete':
            return self.delete_user(request)
        elif action == 'update':
            return self.update_user_field(request)
        elif action == 'get_all':
            return self.get_all_users(request)
        elif action == 'get_user':
            return self.get_user_by_lab_and_date(request)
        else:
            return Response({'error': 'Неверное действие'}, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
            'number': openapi.Schema(type=openapi.TYPE_STRING, description='Number'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
            'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role name'),
            'lab': openapi.Schema(type=openapi.TYPE_INTEGER, description='Lab ID'),
            'telegram_id': openapi.Schema(type=openapi.TYPE_STRING, description='Telegram ID'),
            'orders_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='Orders count'),
            'permissions': openapi.Schema(type=openapi.TYPE_STRING, description='Permissions'),
        }
    ))
    def add_new_user(self, request):
        try:
            data = request.data
            BasicUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                number=data.get('number'),
                email=data.get('email'),
                role=Role.objects.get(role_name=data.get('role')),
                lab=Lab.objects.get(id=data.get('lab')),
                telegram_id=data.get('telegram_id'),
                orders_count=data.get('orders_count'),
                permissions=data.get('permissions')
            )
            return Response({'message': 'User was added'}, status=HTTP_201_CREATED)
        except Role.DoesNotExist:
            return Response({'error': 'Role does not exist'}, status=HTTP_400_BAD_REQUEST)
        except Lab.DoesNotExist:
            return Response({'error': 'Lab does not exist'}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
            # Add other properties as needed for updating specific fields
        }
    ))
    def update_user_field(self, request):
        try:
            user_id = request.data.get('id')
            user = get_object_or_404(BasicUser, id=user_id)

            fields_to_update = ['first_name', 'last_name', 'number', 'email', 'telegram_id', 'orders_count',
                                'permissions', 'username', 'password']
            for field in fields_to_update:
                value = request.data.get(field)
                if value:
                    setattr(user, field, value)

            role_name = request.data.get('role')
            if role_name:
                try:
                    role = Role.objects.get(role_name=role_name)
                    user.role = role
                except Role.DoesNotExist:
                    return Response({'error': 'Role does not exist'}, status=HTTP_400_BAD_REQUEST)

            lab_id = request.data.get('lab')
            if lab_id:
                try:
                    lab = Lab.objects.get(id=lab_id)
                    user.lab = lab
                except Lab.DoesNotExist:
                    return Response({'error': 'Lab does not exist'}, status=HTTP_400_BAD_REQUEST)

            user.save()
            return Response({'message': 'User updated'}, status=HTTP_200_OK)

        except BasicUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
        }
    ))
    def delete_user(self, request):
        try:
            user_id = request.data.get('id')
            user = get_object_or_404(BasicUser, id=user_id)
            user.delete()
            return Response(status=HTTP_204_NO_CONTENT)

        except BasicUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def get_all_users(self, request):
        users = BasicUser.objects.all()
        user_list = list(users.values())
        return Response(user_list)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'lab': openapi.Schema(type=openapi.TYPE_INTEGER, description='Lab ID'),
            'date': openapi.Schema(type=openapi.TYPE_STRING, description='Date'),
        }
    ))
    def get_user_by_lab_and_date(self, request):
        try:
            lab_id = request.data.get('lab')
            date = request.data.get('date')

            if lab_id and date:
                users = BasicUser.objects.filter(days__date=date, lab=lab_id)
                user_list = list(users.values())
                return Response(user_list, status=HTTP_200_OK)

        except BasicUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class ScheduleView(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'add':
            return self.add_row_schedule(request)
        elif action == 'delete':
            return self.delete_row_schedule(request)
        elif action == 'update':
            return self.update_row_schedule(request)
        elif action == 'get_all':
            return self.get_all_rows(request)
        elif action == 'get_row':
            return self.get_row_by_id(request)
        else:
            return Response({'error': 'Wrong action'}, status=400)

    @staticmethod
    def add_row_schedule(request):
        try:
            data = request.POST
            Schedule.objects.create(
                employee=BasicUser.objects.get(id=data.get('employee')),
                lab=Lab.objects.get(id=data.get('lab')),
                date=datetime.strptime(data.get('date'), '%Y-%m-%d')
            )
            return Response({'message': 'Row was added'})
        except Lab.DoesNotExist:
            return Response({'error': 'Lab does not exist'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @staticmethod
    def delete_row_schedule(request):
        try:
            row = get_object_or_404(Schedule, id=request.POST.get('id'))
            row.delete()
            return HttpResponse("{status: 200}")

        except BasicUser.DoesNotExist:
            return Response({'error': 'Row does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @staticmethod
    def update_row_schedule(request):
        try:
            row_id = request.POST.get('id')
            row = get_object_or_404(Schedule, id=row_id)
            date = request.POST.get('date')
            if date:
                row.date = date
            user_id = request.POST.get('employee')
            if user_id:
                user = BasicUser.objects.get(id=user_id)
                if user:
                    row.employee = user
            lab_id = request.POST.get('lab')
            if lab_id:
                lab = Lab.objects.get(id=lab_id)
                if lab:
                    row.lab = lab
            row.save()
            return Response({'message': 'Row updated'})
        except BasicUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @staticmethod
    def get_all_rows(request):
        rows = Schedule.objects.all()
        rows_list = list(rows.values())

        return Response(rows_list)

    @staticmethod
    def get_row_by_id(request):
        try:
            data = request.POST
            row_id = data.get('id')
            if row_id:
                row = Schedule.objects.get(id=row_id)
                row_dict = model_to_dict(row)
                return JsonResponse(row_dict, safe=False)

        except BasicUser.DoesNotExist:
            return Response({'error': 'Row does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class OrderView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = None
        self.status_model = None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        type_order = request.POST.get('type')
        if type_order == 'company':
            self.model = CompanyOrder
            self.status_model = CompanyOrderStatus
        elif type_order == 'basic':
            self.model = Order
            self.status_model = OrderStatus

        action = request.POST.get('action')
        if action == 'add':
            return self.add_order(request)
        elif action == 'delete':
            return self.delete_order(request)
        elif action == 'update':
            return self.update_order(request)
        elif action == 'get_all':
            return self.get_all_orders(request)
        elif action == 'get_order':
            return self.get_order_by_id(request)
        else:
            return Response({'error': 'Wrong action'}, status=400)

    def add_order(self, request):
        try:
            data = request.POST
            self.model.objects.create(
                lab=Lab.objects.get(id=data.get('lab')),
                order_name=data.get('order_name'),
                description=data.get('description'),
                status=self.status_model.objects.get(status_name=data.get('status')),
                exec=BasicUser.objects.get(id=data.get('exec')),
                order_creator=BasicUser.objects.get(id=data.get('order_creator')),
                deadline=data.get('deadline')
            )
            return Response({'message': 'Order was added'})
        except Lab.DoesNotExist:
            return Response({'error': 'Lab does not exist'}, status=400)
        except BasicUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def delete_order(self, request):
        try:
            order = get_object_or_404(self.model, id=request.POST.get('id'))
            order.delete()
            return Response("{status: 200}")

        except self.model.DoesNotExist:
            return Response({'error': 'Order does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def update_order(self, request):
        try:
            order_id = request.POST.get('id')
            order = get_object_or_404(self.model, id=order_id)
            order_name = request.POST.get('order_name')
            if order_name:
                order.order_name = order_name
            deadline = request.POST.get('deadline')
            if deadline:
                order.deadline = deadline
            exec_id = request.POST.get('exec')
            if exec_id:
                user = BasicUser.objects.get(id=exec_id)
                if user:
                    order.exec = user
            creator_id = request.POST.get('order_creator')
            if creator_id:
                user = BasicUser.objects.get(id=creator_id)
                if user:
                    order.exec = user
            lab_id = request.POST.get('lab')
            if lab_id:
                lab = Lab.objects.get(id=lab_id)
                if lab:
                    order.lab = lab
            status_name = request.POST.get('status')
            if status_name:
                status = self.status_model.objects.get(status_name=status_name)
                if status:
                    order.status = status
            order.save()
            return Response({'message': 'Order updated'})
        except self.model.DoesNotExist:
            return Response({'error': 'Order does not exist'}, status=404)
        except BasicUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)
        except Lab.DoesNotExist:
            return Response({'error': 'Lab does not exist'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def get_all_orders(self, request):
        orders = self.model.objects.all()
        orders_list = list(orders.values())

        return Response(orders_list)

    def get_order_by_id(self, request):
        try:
            data = request.POST
            order_id = data.get('id')
            if order_id:
                order = self.model.objects.get(id=order_id)
                order_dict = model_to_dict(order)
                return Response(order_dict)

        except BasicUser.DoesNotExist:
            return Response({'error': 'Order does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class NewsView(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'add':
            return self.add_new(request)
        elif action == 'delete':
            return self.delete_new(request)
        elif action == 'update':
            return self.update_new(request)
        elif action == 'get_all':
            return self.get_all_news(request)
        elif action == 'get_new':
            return self.get_new_by_id(request)
        else:
            return Response({'error': 'Wrong action'}, status=400)

    @staticmethod
    def add_new(request):
        try:
            data = request.POST
            News.objects.create(
                news_type=NewsType.objects.get(type=data.get('type')),
                header=data.get('header'),
                content=data.get('content'),
                picture=data.get('picture'),
                telegram_post=data.get('tg_post'),
                editor=BasicUser.objects.get(id=data.get('editor')),
            )
            return Response({'message': 'New was added'})
        except NewsType.DoesNotExist:
            return Response({'error': 'NewsType does not exist'}, status=400)
        except BasicUser.DoesNotExist:
            return Response({'error': 'Editor does not exist'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @staticmethod
    def delete_new(request):
        try:
            row = get_object_or_404(News, id=request.POST.get('id'))
            row.delete()
            return Response("{status: 200}")

        except BasicUser.DoesNotExist:
            return Response({'error': 'New does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @staticmethod
    def update_new(request):
        try:
            new_id = request.POST.get('id')
            new = get_object_or_404(News, id=new_id)

            fields_to_update = ['header', 'picture', 'content', 'tg_post']
            for field in fields_to_update:
                value = request.POST.get(field)
                if value:
                    setattr(new, field, value)

            new_type_id = request.POST.get('new_type')
            if new_type_id:
                user = BasicUser.objects.get(id=new_type_id)
                if user:
                    new.employee = user
            user_id = request.POST.get('editor')
            if user_id:
                user = BasicUser.objects.get(id=user_id)
                if user:
                    new.employee = user
            new.save()
            return Response({'message': 'New updated'})
        except News.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @staticmethod
    def get_all_news(request):
        news = News.objects.all()
        news_list = list(news.values())

        return Response(news_list)

    @staticmethod
    def get_new_by_id(request):
        try:
            data = request.POST
            new_id = data.get('id')
            if new_id:
                new = News.objects.get(id=new_id)
                new_dict = model_to_dict(new)
                return Response(new_dict)

        except News.DoesNotExist:
            return Response({'error': 'New does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class LoginView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['username', 'password'],
        )
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password.'}, status=400)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=401)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view.'})
