from django.db import models
from datetime import date,datetime
# Create your models here.

class Category_Model(models.Model):
  categories = models.CharField(max_length = 250)
  
  def __str__(self):
    return self.categories


status_choice = [
  ('completed','Completed'),
  ('pending','Pending'),
  ]

class Todo_Task_Model(models.Model):
  category = models.ForeignKey(Category_Model, related_name = "tasks",on_delete = models.CASCADE,null = True, blank = True)
  task = models.CharField(max_length = 250)
  status = models.CharField(max_length = 50, choices = status_choice, default = "pending")
  created_on = models.DateTimeField(auto_now_add = True)
  due_on = models.DateField(null = True, blank = True)
  
  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f'Task : {self.task} ({self.status})'
    
  