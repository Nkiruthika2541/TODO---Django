from django import forms
from todo_app.models import Todo_Task_Model

class Todo_Task_Form(forms.ModelForm):
  class Meta:
    model = Todo_Task_Model
    fields = ['task','status','due_on']
    widgets = {
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
    fields = ['task','status','due_on']
    