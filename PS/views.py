from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from PS.models import BasicUser, Role, Lab, Schedule
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


def get_all_users(request):
    users = BasicUser.objects.all()
    user_list = list(users.values())

    return JsonResponse(user_list, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def add_new_user(request):
    if request.method == 'POST':
        try:
            data = request.POST
            BasicUser.objects.create(
                first_name=data.get('first_name'),
                surname=data.get('surname'),
                number=data.get('number'),
                email=data.get('email'),
                role=Role.objects.get(role_name=data.get('role')),
                lab=Lab.objects.get(lab_name=data.get('lab')),
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
    else:
        return JsonResponse({'error': 'Request method not allowed'}, status=405)


@csrf_exempt
def delete_user(request):
    if request.method == 'POST':
        try:
            user = get_object_or_404(BasicUser, id=request.POST.get('id'))
            user.delete()
            return HttpResponse("{status: 200}")

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Request method not allowed'}, status=405)


@csrf_exempt
def update_user_field(request):
    if request.method == 'POST':
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

            lab_name = request.POST.get('lab')
            if lab_name:
                lab = Lab.objects.get(lab_name=lab_name)
                if lab:
                    user.lab = lab

            user.save()
            return JsonResponse({'message': 'User updated'})

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Request method not allowed'}, status=405)


@csrf_exempt
def add_row_schedule(request):
    if request.method == 'POST':
        try:
            data = request.POST
            Schedule.objects.create(
                employee=BasicUser.objects.get(id=data.get('employee_id')),
                lab=Lab.objects.get(lab_name=data.get('lab')),
                date=datetime.strptime(data.get('date'), '%Y-%m-%d')
            )
            return JsonResponse({'message': 'Schedule updated'})
        except Lab.DoesNotExist:
            return JsonResponse({'error': 'Lab does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Request method not allowed'}, status=405)


@csrf_exempt
def get_user_by_lab_and_date(request):
    if request.method == 'POST':
        try:
            data = request.POST
            if data.get('lab') and data.get('date'):
                users = BasicUser.objects.filter(days__date=data.get('date'), lab=data.get('lab'))
                return JsonResponse(list(users.values()), safe=False)

        except BasicUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Request method not allowed'}, status=405)
