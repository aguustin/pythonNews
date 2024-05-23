from django.db import models
from django.forms import model_to_dict

# Create your models here.

class User(models.Model):
    profile = models.FileField(upload_to="users_profiles", null=True, blank=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    userType = models.IntegerField()

    def __str__(self):
        return self.mail
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'Users'
        ordering = ['id']