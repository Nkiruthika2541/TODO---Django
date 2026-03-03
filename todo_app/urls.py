from django.urls import path
from todo_app import views

urlpatterns = [
  path('hello/',views.hello,name="hello"),
  path('home/',views.home,name="home"),
  path('create/',views.create,name="create"),
  path('update/<int:task_id>/',views.update,name="update"),
  path('delete/<int:task_id>/',views.delete,name="delete"),
  
  ]