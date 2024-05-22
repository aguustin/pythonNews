"""
URL configuration for news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django import views
from users import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', csrf_exempt(views.Create_User.as_view()), name="createUser"),
    path('getUserById/<int:id>/', views.Get_User_By_Id.as_view(), name="get_user_by_id"),
    path('deleteUser/<int:id>/', views.Delete_User.as_view(), name="delete_user"),
    path('updateUser/', csrf_exempt(views.Update_User_Info.as_view()), name="update_user")
]
