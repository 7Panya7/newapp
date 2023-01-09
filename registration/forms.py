from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput
from .models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'login', 'age', 'email', 'password']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'

            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'

            })
        }