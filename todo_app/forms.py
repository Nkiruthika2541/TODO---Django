from django import forms
from todo_app.models import Todo_Task_Model

class Todo_Task_Form(forms.ModelForm):
  class Meta:
    model = Todo_Task_Model
    fields = '__all__'

class Update_Task_Form(forms.ModelForm):
  class Meta:
    model = Todo_Task_Model
    fields = ['task','status','due_on']
    