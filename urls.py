from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('categories/', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('register/', views.register, name='register'),
]