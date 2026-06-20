from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ad/create/', views.ad_create, name='ad_create'),
    path('ad/<int:pk>/update/', views.ad_update, name='ad_update'),
    path('ad/<int:pk>/delete/', views.ad_delete, name='ad_delete'),
]
