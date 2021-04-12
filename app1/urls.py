"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', views.Register.as_view(), name='register'),
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task'),
    path('create-task', views.TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>', views.TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>', views.TaskDelete.as_view(), name='delete-task'),

]
