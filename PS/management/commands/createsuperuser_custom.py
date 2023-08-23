from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from PS.models import BasicUser, Lab, Role


class Command(createsuperuser.Command):
    # временное решение
    def handle(self, *args, **options):
        username = input("username ")
        password = input("password ")
        lab = input("lab")
        role = input("role")

        if not lab or not role:
            raise CommandError("Необходимо предоставить значения для обязательных полей.")

        try:
            user = BasicUser.objects.create_superuser(username=username, password=password, lab=Lab.objects.get(id=lab),
                                                      role=Role.objects.get(id=lab))
            self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан!'))
        except Exception as e:
            raise CommandError("Ошибка при создании суперпользователя: {}".format(e))
