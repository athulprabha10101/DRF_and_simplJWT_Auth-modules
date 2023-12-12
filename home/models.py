from unicodedata import category
from django.db import models
from django.forms import CharField


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default = 18)
    stream = models.CharField(max_length=50)

class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Books(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)