from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import RegisterForm, LoginForm, AdForm
from .models import Ad


def home_view(request):
    """Главная страница"""
    return render(request, 'home.html')


def register_view(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('ads:home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """Вход пользователя"""
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ads:home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """Выход пользователя"""
    logout(request)
    return redirect('ads:login')


{"text": "def ad_list(request):\n    \"\"\"Список всех объявлений\"\"\"\n    ads = Ad.objects.all()\n    return render(request, 'ads/ad_list.html', {'ads': ads})\n\n\ndef ad_detail(request, pk):\n    \"\"\"Детальный просмотр объяв��ения\"\"\"\n    ad = get_object_or_404(Ad, pk=pk)\n    return render(request, 'ads/ad_detail.html', {'ad': ad})"}


@login_required
def ad_create(request):
    """Создание объявления"""
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            return redirect('ads:ad_detail', pk=ad.pk)
    else:
        form = AdForm()
    return render(request, 'ads/ad_create.html', {'form': form})


@login_required
def ad_update(request, pk):
    """Редактирование объявления"""
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ads:ad_detail', pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_update.html', {'form': form, 'ad': ad})


@login_required
def ad_delete(request, pk):
    """Удаление объявления"""
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ads:ad_list')
    return render(request, 'ads/ad_delete.html', {'ad': ad})
