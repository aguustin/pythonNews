import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from users.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.

class Create_User(CreateView): #funciona
    model = User

    def post(self, request, *args, **kwargs):
        post_profile = request.FILES.get('profile')
        post_firstName = request.POST.get('firstName')
        post_lastName = request.POST.get('lastName')
        post_mail = request.POST.get('mail')
        post_password = request.POST.get('password')
        post_userType = request.POST.get('userType')

        save_user = User.objects.create(profile=post_profile, firstName=post_firstName, lastName=post_lastName, mail=post_mail, password=post_password, userType=post_userType)
        save_user.save()

        return HttpResponse(200)
    

    
class Get_User_By_Id(ListView): #funciona
    model = User

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('userId')
        get_user_info = list(User.objects.filter(id=user_id).values())
        print(get_user_info)
        return JsonResponse(get_user_info, safe=False)
    

    
class Delete_User(DeleteView):
    model = User

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('userId')
        User.objects.filter(id=user_id).delete()

        return HttpResponse(200)
    


class Update_User_Info(CreateView): #funciona
    model = User

    def post(self, request, *args, **kwargs):
        get_id = request.POST.get('userId')
        update_profile = request.FILES.get('profile')
        update_firstname = request.POST.get('firstName')
        update_lastname = request.POST.get('lastName')
        update_mail = request.POST.get('mail')

        user_instance = User.objects.get(id=get_id)

        user_instance.profile = update_profile
        user_instance.firstName = update_firstname
        user_instance.lastName = update_lastname
        user_instance.mail = update_mail

        user_instance.save(update_fields=['profile', 'firstName', 'lastName', 'mail'])
        return HttpResponse(200)
    
