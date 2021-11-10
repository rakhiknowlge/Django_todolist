from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def list_todo_items(request):
  #  return HttpResponse("<h1> from list_todo_items </h1>")
    context = {'todo_list': Todo.objects.all()}
    return render(request,'todos/todo_list.html',context)

def insert_todo_item(request:HttpResponse):
  # return render(request, 'todos/todo_list.html')

  todo =Todo(content= request.POST['content'])
  todo.save()

  return redirect('/todos/list')

def delete_todo_item(request,todo_id):
  todo_to_delete= Todo.objects.get(id=todo_id)
  todo_to_delete.delete()

  return redirect('/todos/list')