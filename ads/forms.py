from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Ad


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""
    email = forms.EmailField(required=False, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убираем подсказки пароля
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class LoginForm(AuthenticationForm):
    """Форма входа пользователя"""
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class AdForm(forms.ModelForm):
    """Форма объявления"""
    class Meta:
        model = Ad
        fields = ('title', 'description', 'price', 'image', 'category', 'car_brand')
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'price': 'Цена',
            'image': 'Изображение',
            'category': 'Категория',
            'car_brand': 'Бренд',
        }
        help_texts = {
            'category': 'Выберите тип автомобиля',
            'car_brand': 'Выберите марку автомобиля',
        }
        


class AdFilterForm(forms.Form):
    """Форма фильтрации объявлений"""
    category = forms.ChoiceField(
        choices=[('', 'Все категории')] + Ad.CAR_CATEGORIES,
        required=False,
        label='Категория'
    )
    car_brand = forms.ChoiceField(
        choices=[('', 'Все бренды')] + Ad.CAR_BRANDS,
        required=False,
        label='Бренд'
    )
    search = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={'placeholder': 'Поиск по названию или описанию'})
    )
