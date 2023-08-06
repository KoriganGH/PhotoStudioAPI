from django.conf import settings
from django.conf.urls.static import static

from PS.views import *
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin', admin.site.urls),
    path('user/create', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('user/list', UserListView.as_view(), name='user_list'),
    path('user/lab_list', UserLabListView.as_view(), name='user_lablist'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('schedule/', ScheduleView.as_view(), name='schedule-management'),
    path('orders/', OrderView.as_view(), name='orders-management'),
    path('news/', NewsView.as_view(), name='news-management'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
