from django.contrib import admin
from django.urls import path
from PS.views import UserView, ScheduleView, OrderView, NewsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserView.as_view(), name='user-management'),
    path('schedule/', ScheduleView.as_view(), name='schedule-management'),
    path('orders/', OrderView.as_view(), name='orders-management'),
    path('news/', NewsView.as_view(), name='news-management'),
    path('add/', UserView.add_new_user, name='add_user')
    # path('update/<int:user_id>/', UserView.update_user_field, name='update_user')
]