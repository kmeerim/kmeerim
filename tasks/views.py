# from django.shortcuts import render, redirect
# from tasks.models import Task
#
#
# def get_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         return render(request, 'index.html', {"tasks": tasks})
from django.shortcuts import render, redirect

from Todo.tasks.models import Task


def get_list(reguest):
    if reguest.method == 'GET':
        tasks = Task.objects.filter(is_activate=True).order_by('-id')
        return render(reguest, 'index.html', {"tasks": tasks})


def create_task(reguest):
    if reguest.method == 'POST':
        title = reguest.POST.get('title')
        description = reguest.POST.get('description')
        created_at = reguest.POST.get('created_at')
        type = reguest.POST.get('type')
        task = Task.objects.create(title=title, description=description, created_at=created_at, type=type)
        return redirect('index')
    return render(reguest, 'index.html')


def update_task(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        type: object = request.POST.get('type')
        task = Task.objects.filter(id=id, is_active=True).first()
        task.title = title
        task.description = description
        task.created_at = created_at
        task.type = type
        task.save()
        return redirect('index')
    context = {
        'data': Task.objects.get(id=id)
    }
    return render(request, 'update.html')


def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id, is_active=True)
        task.is_active = False
        task.save()
        task.delete()
        return redirect('index')
    return render(request, 'index.html')
