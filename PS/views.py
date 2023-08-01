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


class UserView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        action = request.POST.get('action')
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
            return JsonResponse({'error': 'Wrong action'}, status=400)

    @staticmethod
    def add_new_user(request):
        try:
            data = request.POST
            print(data.get('password'))
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
            return JsonResponse({'message': 'User was added'})
        except Role.DoesNotExist:
            return JsonResponse({'error': 'Role does not exist'}, status=400)
        except Lab.DoesNotExist:
            return JsonResponse({'error': 'Lab does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def delete_user(request):
        try:
            user = get_object_or_404(BasicUser, id=request.POST.get('id'))
            user.delete()
            return HttpResponse("{status: 200}")

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def update_user_field(request):
        try:
            user_id = request.POST.get('id')
            user = get_object_or_404(BasicUser, id=user_id)

            fields_to_update = ['first_name', 'surname', 'number', 'email', 'telegram_id', 'orders_count',
                                'permissions']
            for field in fields_to_update:
                value = request.POST.get(field)
                if value:
                    setattr(user, field, value)

            role_name = request.POST.get('role')
            if role_name:
                role = Role.objects.get(role_name=role_name)
                if role:
                    user.role = role

            lab_id = request.POST.get('lab')
            if lab_id:
                lab = Lab.objects.get(id=lab_id)
                if lab:
                    user.lab = lab

            user.save()
            return JsonResponse({'message': 'User updated'})

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def get_all_users(request):
        users = BasicUser.objects.all()
        user_list = list(users.values())

        return JsonResponse(user_list, safe=False, json_dumps_params={'ensure_ascii': False})

    @staticmethod
    def get_user_by_lab_and_date(request):
        try:
            data = request.POST
            if data.get('lab') and data.get('date'):
                users = BasicUser.objects.filter(days__date=data.get('date'), lab=data.get('lab'))
                return JsonResponse(list(users.values()), safe=False)

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class ScheduleView(View):
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
            return JsonResponse({'error': 'Wrong action'}, status=400)

    @staticmethod
    def add_row_schedule(request):
        try:
            data = request.POST
            Schedule.objects.create(
                employee=BasicUser.objects.get(id=data.get('employee')),
                lab=Lab.objects.get(id=data.get('lab')),
                date=datetime.strptime(data.get('date'), '%Y-%m-%d')
            )
            return JsonResponse({'message': 'Row was added'})
        except Lab.DoesNotExist:
            return JsonResponse({'error': 'Lab does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def delete_row_schedule(request):
        try:
            row = get_object_or_404(Schedule, id=request.POST.get('id'))
            row.delete()
            return HttpResponse("{status: 200}")

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'Row does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

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
            return JsonResponse({'message': 'Row updated'})
        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def get_all_rows(request):
        rows = Schedule.objects.all()
        rows_list = list(rows.values())

        return JsonResponse(rows_list, safe=False, json_dumps_params={'ensure_ascii': False})

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
            return JsonResponse({'error': 'Row does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class OrderView(View):
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
            return JsonResponse({'error': 'Wrong action'}, status=400)

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
            return JsonResponse({'message': 'Order was added'})
        except Lab.DoesNotExist:
            return JsonResponse({'error': 'Lab does not exist'}, status=400)
        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete_order(self, request):
        try:
            order = get_object_or_404(self.model, id=request.POST.get('id'))
            order.delete()
            return HttpResponse("{status: 200}")

        except self.model.DoesNotExist:
            return JsonResponse({'error': 'Order does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

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
            return JsonResponse({'message': 'Order updated'})
        except self.model.DoesNotExist:
            return JsonResponse({'error': 'Order does not exist'}, status=404)
        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Lab.DoesNotExist:
            return JsonResponse({'error': 'Lab does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_all_orders(self, request):
        orders = self.model.objects.all()
        orders_list = list(orders.values())

        return JsonResponse(orders_list, safe=False, json_dumps_params={'ensure_ascii': False})

    def get_order_by_id(self, request):
        try:
            data = request.POST
            order_id = data.get('id')
            if order_id:
                order = self.model.objects.get(id=order_id)
                order_dict = model_to_dict(order)
                return JsonResponse(order_dict, safe=False, json_dumps_params={'ensure_ascii': False})

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'Order does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class NewsView(View):
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
            return JsonResponse({'error': 'Wrong action'}, status=400)

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
            return JsonResponse({'message': 'New was added'})
        except NewsType.DoesNotExist:
            return JsonResponse({'error': 'NewsType does not exist'}, status=400)
        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'Editor does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def delete_new(request):
        try:
            row = get_object_or_404(News, id=request.POST.get('id'))
            row.delete()
            return HttpResponse("{status: 200}")

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'New does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

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
            return JsonResponse({'message': 'New updated'})
        except News.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    @staticmethod
    def get_all_news(request):
        news = News.objects.all()
        news_list = list(news.values())

        return JsonResponse(news_list, safe=False, json_dumps_params={'ensure_ascii': False})

    @staticmethod
    def get_new_by_id(request):
        try:
            data = request.POST
            new_id = data.get('id')
            if new_id:
                new = News.objects.get(id=new_id)
                new_dict = model_to_dict(new)
                return JsonResponse(new_dict, safe=False)

        except News.DoesNotExist:
            return JsonResponse({'error': 'New does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
#
#
# class LoginView(APIView):
#     permission_classes = []
#
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         if username is None or password is None:
#             return Response({'error': 'Please provide both username and password.'}, status=400)
#
#         user = authenticate(username=username, password=password)
#
#         if user is None:
#             return Response({'error': 'Invalid credentials.'}, status=401)
#
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)
#
#         return Response({'access_token': access_token})
#
#
# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         return Response({'message': 'This is a protected view.'})
