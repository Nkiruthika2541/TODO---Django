from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from todo_app.forms import Todo_Task_Form, Update_Task_Form, Category_Form
from todo_app.models import Todo_Task_Model, Category_Model

# Create your views here.
def hello(request):
  return HttpResponse("<h1>Hello Kiruthi,</h1>\n<h2>Starting TODO Application Now</h2>\n<h3>All the Best</h3>")

  
def home(request):
  tasks = Todo_Task_Model.objects.all().order_by('-created_on')
  return render(request,'HOME.html',{'tasks':tasks})
  
def create(request):
  if request.method=="POST":
    form = Todo_Task_Form(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Task Added Successfully')
      return redirect('home')
  else:
    form = Todo_Task_Form()
    
  return render(request,'Create.html',{"form":form})
  
def category(request):
  if request.method == "POST":
    form = Category_Form(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Category Created Successfully')
      return redirect('home')
  else:
    form = Category_Form()
    
  return render(request,'Category.html',{'form':form})
  
  
  
def update(request,task_id):
  update_task = Todo_Task_Model.objects.get(id=task_id)
  if request.method=="POST":
    form = Update_Task_Form(request.POST,instance=update_task)
    if form.is_valid():
      form.save()
      messages.success(request,'Task Updated Successfully')
      return redirect('home')
  else:
    form = Todo_Task_Form(instance=update_task)
    
  return render(request,'Update.html',{"form":form})
  
def delete(request,task_id):
  delete_task = Todo_Task_Model.objects.get(id=task_id)
  if request.method == 'POST':
      delete_task.delete()
      messages.success(request,'Task deleted Successfully')
      return redirect('home')
  else:
    messages.error(request,"Task doesn't exist.")
  return render(request,'Delete.html',{'delete_task':det})
    
  
