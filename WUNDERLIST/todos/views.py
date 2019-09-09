from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    # data 가져오기
    title = request.POST.get('title')
    due_date = request.POST.get('due-date')

    Todo.objects.create(title=title, due_date=due_date)
    return redirect('todos:index')

def edit(request, pk):
    # 기존 data 가져오기
    todo = Todo.objects.get(id=pk)
    context = {
        'todo': todo
    }

    return render(request, 'todos/edit.html',context)


def update(request, pk):
    # 갱신된 최신 data 가져오기
    title = request.POST.get('title')
    due_date = request.POST.get('due-date')

    todo = Todo.objects.get(id=pk)
    todo.title = title
    todo.due_date = due_date
    todo.save()

    return redirect('todos:index')

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todos:index')