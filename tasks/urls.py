from django.urls import path
from . import views 

urlpatterns = [
    
    path('signup/', views.signup_view, name='signup_view'), 
    path('login/', views.login_view, name='login_view'),
    path('my-todo/', views.my_todo_view, name='my_todo_view'),
    path('createtask/', views.create_task_view, name='create_task_view'),
    path('deletetask/<int:pk>/', views.delete_task_view, name='delete_task_view'),
    path('updatetask/<int:pk>/', views.edit_task_view, name='update_task_view'),
    path('firstpage/', views.firstpage, name='firstpage'),
    
    
]