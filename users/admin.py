from django.contrib import admin

from users.models import User

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
        list_display = [
            'id',
            'profile',
            'firstName',
            'lastName',
            'mail',
            'password',
            'userType'
        ]
        
admin.site.register(User, UsersAdmin)