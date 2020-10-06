from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from daytasks.models import TodoList
from .forms import SignUpForm


@login_required
def home(request):
    user = request.user
    todolist = TodoList.objects.filter(user=user)
    return render(request, 'home.html', {'todo': todolist})


@login_required
def delete(request, task_id):
    todo = TodoList.objects.get(id=task_id)
    todo.delete()
    return redirect('home')


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        due_date = request.POST['due_date']
        status = request.POST['status']
        new_task = ToDoList.objects.create(title=title, content=content, due_date=due_date, status=status)
        new_task.save()

        return redirect('home')
    #     todo = TodoList(id=task_id)
    # return redirect('home')


@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        due_date = request.POST['due_date']
        status = request.POST['status']
        new_task = ToDoList.objects.get(id=task_id)
        new_task.title = title
        new_task.content = content
        new_task.due_date = due_date
        new_task.status = status
        new_task.save()

        return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
