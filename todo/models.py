from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(default=timezone.now)
    completion_time = models.DateTimeField(default=timezone.now)
    task_status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.task_name