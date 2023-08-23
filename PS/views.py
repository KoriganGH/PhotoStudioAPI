from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, \
    HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: 'Авторизация успешна.',
            401: 'Неверные учетные данные.',
            400: 'Пожалуйста, предоставьте имя пользователя и пароль.'
        }
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Пожалуйста, предоставьте имя пользователя и пароль.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Авторизация успешна.'})
        else:
            return Response({'error': 'Неверные учетные данные.'}, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    """
        Operations with users.

        This viewset provides CRUD operations for managing users.

        retrieve:
        Retrieve a user instance.

        list:
        Retrieve a list of users.

        create:
        Create a new user instance.

        update:
        Update a user instance.

        partial_update:
        Partially update a user instance.

        destroy:
        Delete a user instance.

        schedule_filter:
        Filter users by schedule date and lab.
    """

    queryset = BasicUser.objects.all()
    serializer_class = UserDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        elif self.action in ['retrieve', 'destroy']:
            return UserDetailSerializer
        return super().get_serializer_class()

    @swagger_auto_schema(
        method='get',
        manual_parameters=[
            openapi.Parameter('date', openapi.IN_QUERY, description="The date in the schedule.",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('lab', openapi.IN_QUERY, description="The lab name.", type=openapi.TYPE_STRING),
        ],
        responses={HTTP_200_OK: UserDetailSerializer(many=True)},
    )
    @action(detail=False, methods=['get'], url_path='schedule-filter')
    def schedule_filter(self, request):
        """
            Filter users by schedule date and lab.

            This endpoint allows filtering users based on their schedule date and lab.

            Parameters:
            - date (str): The date in the schedule.
            - lab (str): The lab name.

            Example: /api/users/schedule-filter/?date=2023-08-09&lab=LabA
        """
        date = self.request.query_params.get('date', None)
        lab = self.request.query_params.get('lab', None)

        if date and lab:
            queryset = BasicUser.objects.filter(days__date=date, lab=lab)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Please provide both 'date' and 'lab' parameters."},
                            status=HTTP_400_BAD_REQUEST)


class ScheduleViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    """
        Operations with schedule.

        This viewset provides CRUD operations for managing schedule.

        retrieve:
        Retrieve a schedule instance.

        list:
        Retrieve a list of schedules.

        create:
        Create a new schedule instance.

        update:
        Update a schedule instance.

        partial_update:
        Partially update a schedule instance.

        destroy:
        Delete a schedule instance.
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        elif self.action == 'create':
            return ScheduleCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ScheduleUpdateSerializer
        elif self.action in ['retrieve', 'destroy']:
            return ScheduleDetailSerializer
        return super().get_serializer_class()


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    """
        Operations with orders.

        This viewset provides CRUD operations for managing orders.

        retrieve:
        Retrieve an order instance.

        list:
        Retrieve a list of orders.

        create:
        Create a new order instance.

        update:
        Update an order instance.

        partial_update:
        Partially update an order instance.

        destroy:
        Delete an order instance.
    """

    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'create':
            return OrderCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return OrderUpdateSerializer
        elif self.action in ['retrieve', 'destroy']:
            return OrderDetailSerializer
        return super().get_serializer_class()


class CompanyOrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    """
        Operations with company orders.

        This viewset provides CRUD operations for managing company orders.

        retrieve:
        Retrieve a company order instance.

        list:
        Retrieve a list of company orders.

        create:
        Create a new company order instance.

        update:
        Update a company order instance.

        partial_update:
        Partially update a company order instance.

        destroy:
        Delete a company order instance.
    """

    queryset = CompanyOrder.objects.all()
    serializer_class = CompanyOrderDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyOrderListSerializer
        elif self.action == 'create':
            return CompanyOrderCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CompanyOrderUpdateSerializer
        elif self.action in ['retrieve', 'destroy']:
            return CompanyOrderDetailSerializer
        return super().get_serializer_class()


class NewsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    """
        Operations with news.

        This viewset provides CRUD operations for managing news.

        retrieve:
        Retrieve a news instance.

        list:
        Retrieve a list of news.

        create:
        Create a new news instance.

        update:
        Update a news instance.

        partial_update:
        Partially update a news instance.

        destroy:
        Delete a news instance.
    """

    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListSerializer
        elif self.action == 'create':
            return NewsCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return NewsUpdateSerializer
        elif self.action in ['retrieve', 'destroy']:
            return NewsDetailSerializer
        return super().get_serializer_class()

