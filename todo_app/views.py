from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from todo_app.forms import Todo_Task_Form, Update_Task_Form, Category_Form
from todo_app.models import Todo_Task_Model, Category_Model

# Create your views here.
def hello(request):
  return HttpResponse("<h1>Hello Kiruthi,</h1>\n<h2>Starting TODO Application Now</h2>\n<h3>All the Best</h3>")

  
def home(request):
  tasks = Todo_Task_Model.objects.all().order_by('-created_on')
  category = Category_Model.objects.all()
  return render(request,'HOME.html',{'tasks':tasks,'category':category})
  
def create(request):
  category = Category_Model.objects.all()
  if request.method=="POST":
    form = Todo_Task_Form(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Task Added Successfully')
      return redirect('home')
  else:
    form = Todo_Task_Form()
  
  return render(request,'Create.html',{"form":form,'category':category})
  
def category(request):
  category = Category_Model.objects.all()
  if request.method == "POST":
    form = Category_Form(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Category Created Successfully')
      return redirect('home')
  else:
    form = Category_Form()
    
  return render(request,'Category.html',{'form':form,'category':category})
  
  
def update(request,task_id):
  category = Category_Model.objects.all()
  update_task = get_object_or_404(Todo_Task_Model, id=task_id)
  if request.method=="POST":
    form = Update_Task_Form(request.POST,instance=update_task)
    if form.is_valid():
      form.save()
      messages.success(request,'Task Updated Successfully')
      return redirect('home')
  else:
    form = Todo_Task_Form(instance=update_task)
    
  return render(request,'Update.html',{"form":form,'category':category})
  
def delete(request,task_id):
  category = Category_Model.objects.all()
  delete_task = get_object_or_404(Todo_Task_Model, id=task_id)
  if request.method == 'POST':
      delete_task.delete()
      messages.success(request,'Task deleted Successfully')
      return redirect('home')
  return render(request,'Delete.html',{'delete_task':delete_task,'category':category})
    
  
def category_view(request,category_id):
  category = Category_Model.objects.all()
  tasks = Todo_Task_Model.objects.filter(category_id = category_id)
  from_category = get_object_or_404(Category_Model, id=category_id)
  return render(request,'By_Category.html',{'tasks':tasks,'category':category,"from_category":from_category})

def status_view(request,status):
  category = Category_Model.objects.all()
  tasks = Todo_Task_Model.objects.filter(status = status)
  from_status = status.capitalize()
  print(from_status)
  return render(request,'By_Status.html',{'tasks':tasks,'category':category,'from_status':from_status})

def category_edit(request):
  category = Category_Model.objects.all()
  return render(request,'Edit_Category.html',{'category':category})
  
def category_delete(request):
  category = Category_Model.objects.all()
  if request.method == "POST":
    checked_items = request.POST.getlist('category')
    Category_Model.objects.filter(id__in = checked_items).delete()
    return redirect('home')
  return render(request,'Edit_Category.html',{'category':category})