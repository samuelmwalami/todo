from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    COMPLETED = 'completed'
    
    

# Create your views here.

def create_task(request):
    if request.method == 'GET':
        return render(request, 'todo/createForm.html')
    elif request.method == 'POST':
        task_name = request.POST['taskname']
        start_time = datetime.strptime(request.POST['starttime'],'%Y-%m-%dT%H:%M')
        completion_time = datetime.strptime(request.POST['completiontime'],'%Y-%m-%dT%H:%M')
        task_status = TaskStatus.INACTIVE.value
        
        print(task_name,start_time,completion_time,task_status,sep='\n')
        
        new_task = Task.objects.create(task_name=task_name,start_time=start_time,completion_time=completion_time,task_status=task_status)
        new_task.save()
        return redirect('create')

def delete_task(request, taskid):
    task= Task.objects.get(id=taskid)
    task.delete()
    return redirect('inactive')


def inactive_task_view(request):
    status= TaskStatus.INACTIVE.value
    tasks = Task.objects.filter(task_status=status)
    print(tasks,status)
    context = {"tasks" : tasks,
               "status" : status}
    return render(request, 'todo/view.html', context)

def active_task_view(request):
    status= TaskStatus.ACTIVE.value
    tasks = Task.objects.filter(task_status=status)
    context = {"tasks" : tasks,
               "status" : status}
    return render(request, 'todo/view.html', context)

def completed_task_view(request):
    status= TaskStatus.COMPLETED
    completed_tasks = Task.objects.filter(task_status=status)
    context = {"tasks" : completed_tasks,
               "status" : status}
    return render(request, 'todo/view.html',context)

def edit_task(request, taskid):
    if request.method == 'GET':
        task = Task.objects.filter(id=taskid)
        context ={
            'task' : task
        }
        print(task)
        return render(request, 'todo/editForm.html', context)
    elif request.method == 'POST':
        task_name = request.POST['taskname']
        start_time = datetime.strptime(request.POST['starttime'],'%Y-%m-%dT%H:%M')
        completion_time = datetime.strptime(request.POST['completiontime'],'%Y-%m-%dT%H:%M')
        if completion_time > start_time:
            return redirect('edit')
        #task_status = TaskStatus.INACTIVE.value
        
        task = Task.objects.get(id=taskid)
        task.task_name = task_name
        task.start_time = start_time
        task.completion_time = completion_time
        task.save()
        return redirect('inactive')


 
def home(request):
    tasks = Task.objects.all()
    print(tasks,type(tasks))
    context = {
        'tasks' : tasks
    }
    return render(request, 'todo/home.html', context)



