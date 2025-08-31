
from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
]
