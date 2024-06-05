import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import date
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from notices.models import Category, Category_New, New, User_New
from notices.serializers import Category_New_Serializer
from users.models import User
# Create your views here.


class Create_category(CreateView): #funciona
    model = Category

    def post(self, request, *args, **kwargs):
        post_category = request.POST.get('category')

        check_if_category_exists = Category.objects.filter(category=post_category)

        if(check_if_category_exists):
            return HttpResponse(200)
        else:
            category_instance = Category.objects.create(category=post_category)
            category_instance.save()

            return HttpResponse(200)
        

class Upload_New(CreateView): #funciona
    model = User
    model = New
    model = Category
    model = User_New
    model = Category_New

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        data_users = data.get('users_data')
        data_category = data.get('category_data')
        post_title = data.get('title')
        post_subtitle = data.get('subtitle')
        post_imageTitle = request.FILES.get('imageTitle')
        post_firsParagraph = data.get('firstParagraph')
        post_secondParagraph = data.get('secondParagraph')
        post_thirdParagraph = data.get('thirdParagraph')
        post_firstImage = request.FILES.get('firstImage')
        post_secondImage = request.FILES.get('secondImage')
        post_thirdImage = request.FILES.get('thirdImage')
        new_date = date.today()
        print("data_users", data_users)
        new_instance = New.objects.create(title=post_title, 
                                          subtitle=post_subtitle, 
                                          imageTitle=post_imageTitle, 
                                          firstParagraph=post_firsParagraph, 
                                          secondParagraph=post_secondParagraph, 
                                          thirdParagraph=post_thirdParagraph, 
                                          firstImage=post_firstImage, 
                                          secondImage=post_secondImage, 
                                          thirdImage=post_thirdImage,
                                          new_date=new_date)
        new_instance.save()

        for item in data_users:
            user_instance = User.objects.get(mail=item['mail'])
            users_new_instance = User_New.objects.create(
                  user_code=user_instance,
                  new_code=new_instance
            )
            users_new_instance.save()

        for item in data_category:
            category_instance = Category.objects.get(category=item['category'])
            category_new_instance = Category_New.objects.create(
                category_code=category_instance,
                new_code=new_instance
            )
            category_new_instance.save()

        return HttpResponse(200)
    

class Update_New(UpdateView): #probar
    model = New
    model = Category_New
    def post(self, request, *args, **kwargs):
        #data = json.loads(request.body)
        post_id = request.POST.get('newId')
        data_users = request.POST.get('users_data')
        data_category = request.POST.get('category_data')
        post_title = request.POST.get('title')
        post_subtitle = request.POST.get('subtitle')
        post_imageTitle = request.FILES.get('imageTitle')
        post_firstParagraph = request.POST.get('firstParagraph')
        post_secondParagraph = request.POST.get('secondParagraph')
        post_thirdParagraph = request.POST.get('thirdParagraph')
        post_firstImage = request.FILES.get('firstImage')
        post_secondImage = request.FILES.get('secondImage')
        post_thirdImage = request.FILES.get('thirdImage')
        post_new_date = request.POST.get('new_date')

        new_instance = New.objects.get(id=post_id)
        new_instance.title = post_title
        new_instance.subtitle = post_subtitle 
        new_instance.imageTitle = post_imageTitle
        new_instance.firstParagraph = post_firstParagraph
        new_instance.secondParagraph = post_secondParagraph
        new_instance.thirdParagraph = post_thirdParagraph
        new_instance.firstImage = post_firstImage
        new_instance.secondImage = post_secondImage
        new_instance.thirdImage = post_thirdImage
        new_instance.new_date = post_new_date

        new_instance.save(update_fields=['title', 'subtitle', 'imageTitle', 'firstParagraph', 'secondParagraph', 'thirdParagraph', 'firstImage', 'secondImage', 'thirdImage', 'new_date'])

        for item in data_category:
            category_new_instance = Category_New.objects.get(new_code=post_id)
            category_instance = Category.objects.get(category=item['category'])
            category_new_instance.category_code = category_instance
            category_new_instance.save(update_fields=['category_code'])

        for item in data_users:
            user_instance = User.objects.get(mail=item['mail'])
            user_new_instance = User_New.objects.get(new_code=post_id)
            user_new_instance.user_code = user_instance
            user_new_instance.save(update_fields=['user_code'])

        return HttpResponse(200)


class Get_All_News_Categories(ListView): #funciona
    model = Category_New

    def get(self, request, *args, **kwargs):
        get_categories_news = Category_New.objects.all()
        serializer = Category_New_Serializer(get_categories_news, many=True)

        return JsonResponse(serializer.data, safe=False)
    

class Get_New_by_Category_Id(ListView):
    model = Category
    
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('categoryId')
        get_categories = Category.objects.filter(id=category_id).values()

        return JsonResponse(list(get_categories), safe=False)
    

class Get_New_Id(ListView):
    model = New
    model = Category_New

    def get(self, request, *args, **kwargs):
        new_id = kwargs.get('newId')
        get_new = Category_New.objects.get(new_code=new_id)
        print(get_new)
        serializer = Category_New_Serializer(get_new)

        return JsonResponse(serializer.data, safe=False)
    
