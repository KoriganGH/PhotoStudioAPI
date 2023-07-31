from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if kwargs.get('app') == 'PS':
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', '123').save()
