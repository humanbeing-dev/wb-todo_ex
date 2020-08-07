from django.shortcuts import render, redirect
from django.utils import timezone
from todo.models import Todo


def home(request):
    tasks = Todo.objects.all().order_by('-added_date')
    return render(request, 'todo/home.html', context={'tasks': tasks})


def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']

    todo = Todo.objects.create(added_date=current_date, text=content)
    todo.save()
    return redirect('home')


def del_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')
