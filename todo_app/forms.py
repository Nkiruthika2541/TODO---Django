from django import forms
from todo_app.models import Todo_Task_Model, Category_Model

    
class Category_Form(forms.ModelForm):
  class Meta:
    model = Category_Model
    fields = ['categories']
    widgets = {
      'categories' : forms.TextInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Enter the new category'
      })
    }


class Todo_Task_Form(forms.ModelForm):
  class Meta:
    model = Todo_Task_Model
    fields = ['category','task','status','due_on']
    widgets = {
      'category' : forms.Select(attrs = {
        'class' : 'form-select'
      }),
      'task' : forms.TextInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Enter the task'
      }),
      'status' : forms.Select(attrs = {
        'class' : 'form-select'
      }),
      'due_on' : forms.DateInput(attrs = {
        'class' : 'form-control',
        'type' : 'date'
      })
    }

class Update_Task_Form(forms.ModelForm):
  class Meta:
    model = Todo_Task_Model
    fields = ['category','task','status','due_on']
    