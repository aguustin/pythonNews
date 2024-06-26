from django.db import models
from django.forms import model_to_dict
from news import settings
from users.models import User

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    imageTitle = models.FileField(upload_to="news_python")
    firstParagraph = models.TextField()
    secondParagraph = models.TextField()
    thirdParagraph = models.TextField()
    firstImage = models.FileField(upload_to="news_python")
    secondImage = models.FileField(upload_to="news_python")
    thirdImage = models.FileField(upload_to="news_python")
    new_date = models.DateField(null=True)
    
    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['imageTitle'] = self.get_image()
        item['firstImage'] = self.get_image()
        item['secondImage'] = self.get_image()
        item['thirdImage'] = self.get_image()
        return item

    class Meta:
        db_table = 'News'
        ordering = ['id']

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'Category'
        ordering = ['id']

class User_New(models.Model):
    user_code = models.ForeignKey(User,on_delete=models.CASCADE, default="")
    new_code = models.ForeignKey(New, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['user_code'] = self.user_code.toJSON()
        item['new_code'] = self.new_code.toJSON()
        return item
    
    class Meta:
        db_table = 'User_New'
        ordering = ['id']

class Category_New(models.Model):
    category_code = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    new_code = models.ForeignKey(New, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.id)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['category_code'] = self.category_code.toJSON()
        item['new_code'] = self.new_code.toJSON()
        return item
    
    class Meta:
        db_table = 'Categories_and_News'
        ordering = ['id']

