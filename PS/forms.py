from django import forms

from PS.models import Role


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    number = forms.CharField()
    email = forms.EmailField()
    role = forms.ModelChoiceField(queryset=Role.objects.all())
    lab = forms.IntegerField()
    telegram_id = forms.CharField()
    orders_count = forms.IntegerField()
    permissions = forms.CharField()


class UpdateUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    number = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    telegram_id = forms.CharField(required=False)
    orders_count = forms.IntegerField(required=False)
    permissions = forms.CharField(required=False)
    role = forms.ModelChoiceField(queryset=Role.objects.all())
    lab = forms.IntegerField(required=False)
