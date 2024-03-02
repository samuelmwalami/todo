from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_task, name='create'),
    path('edit/<str:taskid>', views.edit_task, name='edit'),
    path('delete/<str:taskid>', views.delete_task, name='delete'),
    path('inactive', views.inactive_task_view, name='inactive'),
    path('active', views.active_task_view, name='active'),
    path('completed', views.completed_task_view, name='completed'),
]