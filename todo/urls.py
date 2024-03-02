from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_task, name='create'),
    path('edit/<str:taskid>', views.task_edit, name='edit'),
    path('inactive', views.inactive_task_view, name='inactive'),
    path('active', views.active_task_view, name='active'),
    path('completed', views.completed_task_view, name='completed'),
]