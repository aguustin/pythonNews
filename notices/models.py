from django.db import models
from django.forms import model_to_dict
from news import settings
from users.models import Users

# Create your models here.

#class Users(models.Model):
   # profile = models.FileField(upload_to="users_profiles")
   # firstName = models.CharField(max_length=20)
   # lastName = models.CharField(max_length=20)
   # mail = models.EmailField(max_length=50)
   # password = models.CharField(max_length=30)
   # userType = models.IntegerField()

    #def __str__(self):
    #    return self.mail
    
    #def toJSON(self):
    #    item = model_to_dict(self)
    #    return item

   # class Meta:
   #     db_table = 'Users'
   #     ordering = ['id']

class News(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    imageTitle = models.FileField(upload_to="news_images")
    firsParagraph = models.TextField()
    secondParagraph = models.TextField()
    thirdParagraph = models.TextField()
    firstImage = models.FileField(upload_to="news_images")
    secondImage = models.FileField(upload_to="news_images")
    thirdImage = models.FileField(upload_to="news_images")

    def __str__(self):
        return self.title
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'News'
        ordering = ['id']

class Categories(models.Model):
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.categories
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'Categories'
        ordering = ['id']

class Users_News(models.Model):
    users_code = models.ForeignKey(Users,on_delete=models.CASCADE, default="")
    news_code = models.ForeignKey(News, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['users_code'] = self.users_code.toJSON()
        item['news_code'] = self.news_code.toJSON()
        return item
    
    class Meta:
        db_table = 'Users_and_News'
        ordering = ['id']

class Categories_News(models.Model):
    categories_code = models.ForeignKey(Categories, on_delete=models.CASCADE, default="")
    news_code = models.ForeignKey(News, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['categories_code'] = self.categories_code.toJSON()
        item['news_code'] = self.news_code.toJSON()
        return item
    
    class Meta:
        db_table = 'Categories_and_News'
        ordering = ['id']

