from django.contrib import admin
from django.urls import path
from PS.views import get_all_users, add_new_user, delete_user, update_user_field, add_row_schedule, get_user_by_lab_or_date

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_new_user/', add_new_user),
    path('all_users/', get_all_users),
    path('delete_user/', delete_user),
    path('update_user/', update_user_field),
    path('schedule_update/', add_row_schedule),
    path('get_user/', get_user_by_lab_or_date)
]
