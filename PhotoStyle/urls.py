from django.contrib import admin
from django.urls import path

from PS import api_info
from PS.views import UserView, ScheduleView, OrderView, NewsView, LoginView
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    api_info.api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserView.as_view(), name='user-management'),
    path('schedule/', ScheduleView.as_view(), name='schedule-management'),
    path('orders/', OrderView.as_view(), name='orders-management'),
    path('news/', NewsView.as_view(), name='news-management'),
    path('add/', UserView.add_new_user, name='add_user'),
    path('login/', LoginView.as_view(), name='login'),
    # path('update/<int:user_id>/', UserView.update_user_field, name='update_user')
    #path('api/', include('your_app.urls')),  # Замените 'your_app.urls' на URL-шаблоны вашего API
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]