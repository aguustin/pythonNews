from django.contrib import admin

from notices.models import Categories, Categories_News, News, Users, Users_News
# Register your models here.

#Users, News, Categories, Users_News, Categories_News


#class UsersAdmin(admin.ModelAdmin):
       # list_display = [
       #     'profile',
       #     'firstName',
      #      'lastName',
      #      'mail',
       #     'password',
      #      'userType'
      #  ]
#admin.site.register(Users, UsersAdmin)


class NewsAdmin(admin.ModelAdmin):
        list_display = [
            'title',
            'subtitle',
            'imageTitle',
            'firsParagraph',
            'secondParagraph',
            'thirdParagraph',
            'firstImage',
            'secondImage',
            'thirdImage'
        ]

admin.site.register(News, NewsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
        list_display = [
            'categories'
        ]

admin.site.register(Categories, CategoriesAdmin)

class Users_News_Admin(admin.ModelAdmin):
        list_display = [
                'users_code',
                'news_code'
        ]

admin.site.register(Users_News, Users_News_Admin)

class Categories_News_Admin(admin.ModelAdmin):
        list_display = [
            'categories_code',
            'news_code'
        ]

admin.site.register(Categories_News, Categories_News_Admin)