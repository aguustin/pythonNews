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

#from django import views
from users import views
from notices import views_notices
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    #users.views
    path('createUser/', csrf_exempt(views.Create_User.as_view()), name="createUser"),
    path('getUserById/<int:userId>/', views.Get_User_By_Id.as_view(), name="get_user_by_id"),
    path('deleteUser/<int:userId>', csrf_exempt(views.Delete_User.as_view()), name="delete_user"),
    path('updateUser/', csrf_exempt(views.Update_User_Info.as_view()), name="update_user"),

    #notices.views
    path('createCategory/', csrf_exempt(views_notices.Create_category.as_view()), name="create_category"),
    path('createNew/', csrf_exempt(views_notices.Create_New.as_view()), name="create_new"),
    path('getAllNews/', views_notices.Get_All_News_Categories.as_view(), name="get_all_new_and_categories"),
    path('getNewByCategory/<int:categoryId>/', views_notices.Get_New_by_Category_Id.as_view(), name="get_news_by_category"),
    path('getNew/<int:newId>/', views_notices.Get_New_Id.as_view(), name="get_new"),
    path('updateNew/', csrf_exempt(views_notices.Update_New.as_view()), name="update_new")
]
