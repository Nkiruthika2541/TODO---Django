from django.db import models
from datetime import date,datetime
# Create your models here.

status_choice = [
  ('1','Select the Status'),
  ('2','Completed'),
  ('3','Not Completed'),
  ]

class Todo_Task_Model(models.Model):
  task = models.CharField(max_length = 250)
  status = models.CharField(max_length = 50, choices = status_choice, default = "1")
  created_on = models.DateTimeField(auto_now_add = True)
  due_on = models.DateField(null = True)
  
  def __str__(self):
    return f'Task : {self.task}\nStatus : {self.status}'