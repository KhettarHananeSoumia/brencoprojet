from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest

from .models import BRENCO

# Create your views here.
def list_todo_items (request):
    context = {'todo_list' : BRENCO.objects.all()}
    return render(request,'brenco/todo_list.html', context)

def insert_todo_item(request: HttpRequest):
    todo = BRENCO(content=request.POST['content'])
    todo.save()
    return redirect('/brenco/list/')

def delete_todo_item(request,todo_id):
    todo_to_delete = BRENCO.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/brenco/list/')