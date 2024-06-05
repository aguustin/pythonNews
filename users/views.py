
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from users.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from cryptography.fernet import Fernet
# Create your views here.

class Create_User(CreateView): #funciona
    model = User

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        post_firstname = data.get('username')
        post_lastname = data.get('lastname')
        post_mail = data.get('mail')
        post_password = data.get('password')
        post_confirm_pass = data.get('confirmPassword')
        user_exists = User.objects.filter(mail=post_mail)
        if user_exists:
            return HttpResponse(412)        #post_userType = request.POST.get('userType')
        if post_password == post_confirm_pass:
            save_user = User.objects.create(firstName=post_firstname, lastName=post_lastname, mail=post_mail, password=post_password, userType=2)
            save_user.save()

            return HttpResponse(200)
        else:
            return HttpResponse(412)
    
    
class Get_In_User(ListView):
    model = User

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_mail = data.get('mail');
        user_pass = data.get('password')
        get_user_instance = User.objects.filter(mail=user_mail).values()
        print(list(get_user_instance))
        if get_user_instance:
            #desencrypt_pass = Fernet.decrypt(get_user_instance.password)
            if user_pass:
                return JsonResponse(list(get_user_instance), safe=False)
            else:
                print('Los password no son iguales')
                return HttpResponse(200)
        else:
            print('el usuario no fue encontrado')
            return HttpResponse(200)   

    
#class Get_User_By_Id(ListView): #funciona
   # model = User

    #def get(self, request, *args, **kwargs):
    #    user_id = kwargs.get('userId')
    #    get_user_info = list(User.objects.filter(id=user_id).values())
    #    print(get_user_info)
    #    return JsonResponse(get_user_info, safe=False)
    

    
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
    
