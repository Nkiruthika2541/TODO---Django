from django.db import models
from datetime import date,datetime
# Create your models here.
class Todo_Task_Model(models.Model):
  task = models.CharField(max_length = 250)
  status = models.BooleanField(default = False)
  created_on = models.DateTimeField(auto_now_add = True)
  due_on = models.DateField(null = True)
  
  def __str__(self):
    return f'Task : {self.task}\nStatus : {self.status}'