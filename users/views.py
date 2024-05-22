import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from users.models import Users
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.

class Create_User(CreateView):
    model = Users

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print('create user', data)

        return HttpResponse(200)
    

    
class Get_User_By_Id(ListView):
    model = Users

    def get(self, request, *args, **kwargs):
        data = kwargs.get('userId')
        get_user_info = list(Users.objects.filter(id=data).values())

        return JsonResponse(get_user_info, safe=False)
    

    
class Delete_User(DeleteView):
    model = Users

    def delete(self, request, *args, **kwargs):
        data = kwargs.get('userId')
        Users.objects.delete(id=data)

        return HttpResponse(200)
    


class Update_User_Info(CreateView):
    model = Users

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        get_id = data.get('userId')
        get_profile = data.get('profile')
        get_firstname = data.get('firstname')
        get_lastname = data.get('lastname')
        get_mail = data.get('mail')

        user_instance = Users.objects.get(id=get_id)

        user_instance.profile = get_profile
        user_instance.firstName = get_firstname
        user_instance.lastName = get_lastname
        user_instance.mail = get_mail

        user_instance.save(update_fields=['profile', 'firstName', 'lastName', 'mail'])
        return HttpResponse(200)
    
