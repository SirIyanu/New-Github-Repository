from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here. 
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


    





