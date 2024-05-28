from django.contrib import admin

from notices.models import Category, Category_New, New, User_New
# Register your models here.

#Users, News, Categories, Users_News, Categories_News


class NewAdmin(admin.ModelAdmin):
        list_display = [
            'title',
            'subtitle',
            'imageTitle',
            'firstParagraph',
            'secondParagraph',
            'thirdParagraph',
            'firstImage',
            'secondImage',
            'thirdImage',
            'new_date'
        ]

admin.site.register(New, NewAdmin)

class CategoryAdmin(admin.ModelAdmin):
        list_display = [
            'category'
        ]

admin.site.register(Category, CategoryAdmin)

class User_New_Admin(admin.ModelAdmin):
        list_display = [
                'user_code',
                'new_code'
        ]

admin.site.register(User_New, User_New_Admin)

class Category_New_Admin(admin.ModelAdmin):
        list_display = [
            'category_code',
            'new_code'
        ]

admin.site.register(Category_New, Category_New_Admin)