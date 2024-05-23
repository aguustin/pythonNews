import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from notices.models import Category, Category_New, New, User_New
from users.models import User
# Create your views here.


class Create_category(CreateView):
    model = Category

    def post(self, request, *args, **kwargs):
        post_category_id = request.POST.get('categoryId')
        post_category = request.POST.get('category')

        if(post_category_id):
            return HttpResponse(200)
        else:
            category_instance = Category.objects.create(category=post_category)
            category_instance.save()

            return HttpResponse(200)

class Create_New(CreateView):
    model = User
    model = New
    model = Category
    model = User_New
    model = Category_New

    def post(self, request, *args, **kwargs):
        data_users = json.loads('users_data')
        data_categories = json.loads('category_data')
        post_title = request.POST.get('title')
        post_subtitle = request.POST.get('subtitle')
        post_imageTitle = request.FILES.get('imageTitle')
        post_firsParagraph = request.POST.get('firstParagraph')
        post_secondParagraph = request.POST.get('secondParagraph')
        post_thirdParagraph = request.POST.get('thirdParagraph')
        post_firstImage = request.FILES.get('firstImage')
        post_secondImage = request.FILES.get('secondImage')
        post_thirdImage = request.FILES.get('thirdImage')
        
        new_instance = New.objects.create(title=post_title, 
                                          subtitle=post_subtitle, 
                                          imageTitle=post_imageTitle, 
                                          firstParagraph=post_firsParagraph, 
                                          secondParagraph=post_secondParagraph, 
                                          thirdParagraph=post_thirdParagraph, 
                                          firstImage=post_firstImage, 
                                          secondImage=post_secondImage, 
                                          thirdImage=post_thirdImage)
        new_instance.save()

        for item in data_users:
            user_instance = User.objects.get(mail=item.mail)
            users_new_instance = User_New.objects.create(
                  user_code=user_instance.id,
                  new_code=new_instance.id
            )
            users_new_instance.save()

        for item in data_categories:
            category_instance = Category.objects.get(category=item.category)
            category_new_instance = Category_New.objects.create(
                category_code=category_instance.id,
                new_code=new_instance.id
            )
            category_new_instance.save()
     