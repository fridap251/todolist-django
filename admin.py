from django.contrib import admin
from .models import Task, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'completed', 'due_date', 'user', 'created_at']
    list_filter = ['completed', 'priority', 'category']
    search_fields = ['title', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'user']
