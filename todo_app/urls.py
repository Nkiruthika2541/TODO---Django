from django.urls import path
from todo_app import views

urlpatterns = [
  path('hello/',views.hello,name="hello"),
  path('home/',views.home,name="home"),
  path('new_task/',views.create,name="create"),
  path('new_category/',views.category,name="category"),
  path('view_by_category/<int:category_id>/',views.category_view,name="category_view"),
  path('edit-category/',views.category_edit,name="category_edit"),
  path('delete-category/',views.category_delete,name="category_delete"),
  path('view_by_status/<str:status>/',views.status_view,name="status_view"),
  path('update/<int:task_id>/',views.update,name="update"),
  path('delete/<int:task_id>/',views.delete,name="delete"),
  
  ]