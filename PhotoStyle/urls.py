from django.contrib import admin
from django.urls import path
from PS.views import get_all_users, add_new_user, delete_user, update_user_field

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_new_user/', add_new_user),
    path('all_users/', get_all_users),
    path('delete_user/', delete_user),
    path('update_user/', update_user_field)
]
