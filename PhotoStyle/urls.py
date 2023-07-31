from django.contrib import admin
from django.urls import path
from PS.views import UserView, ScheduleView, OrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserView.as_view(), name='user-management'),
    path('schedule/', ScheduleView.as_view(), name='schedule-management'),
    path('orders/', OrderView.as_view(), name='orders-management')
]