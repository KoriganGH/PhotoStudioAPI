from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from PS.models import BasicUser, Role
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def get_user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    reviews = BasicUser.objects.all()
    for i in reviews[0].__dict__.items():
        print(i)
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

@csrf_exempt
def test(request):
        print(request.method)
        new_user = BasicUser()

        new_user.first_name = request.POST.get('first_name')
        new_user.surname = request.POST.get('surname')
        new_user.email = request.POST.get('email')
        new_user.number = request.POST.get('number')
        new_user.role = Role.objects.get(id = 1)
        # new_user.role = Role.objects.filter(RoleName = request.POST.get('role'))[0]
        new_user.lab = request.POST.get('lab')
        new_user.permissions = {'sadas': 200}
        new_user.orders_count = 0
        new_user.save()
        return HttpResponse("{status: 200}")

def test2(request):
    reviews = BasicUser.objects.all()
    return reviews[0].login

def basic_user_list(request):
    users = BasicUser.objects.all()
    user_list = list(users.values())

    return JsonResponse(user_list, safe=False)


