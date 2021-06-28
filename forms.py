from .models import Product
from .models import User

from django.forms import ModelForm, TextInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'product',
            'id': 'product',
            'placeholder': 'Введите товар'
            })}


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["password", "mail"]
        widgets = {"password": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'})
        }
