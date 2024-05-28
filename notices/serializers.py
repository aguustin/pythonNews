from rest_framework import serializers

from notices.models import Category, Category_New, New, User_New
from users.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['profile', 'firstName', 'lastName', 'mail', 'password', 'userType']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category']

class NewsSerializer(serializers.ModelSerializer):

    #category_code = CategorySerializer()

    class Meta:
        model = New
        fields = ['title', 'subtitle', 'imageTitle', 'firstParagraph', 'secondParagraph', 'thirdParagraph', 'firstImage', 'secondImage', 'thirdImage', 'new_date']


class User_New_Serializer(serializers.ModelSerializer):

    user_code = UserSerializer()
    new_code = NewsSerializer()

    class Meta:
        model = User_New
        fields = ['user_code', 'new_code']

class Category_New_Serializer(serializers.ModelSerializer):
     
     category_code = CategorySerializer()
     new_code = NewsSerializer()

     class Meta:
         model = Category_New
         fields = ['category_code', 'new_code']