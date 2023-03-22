from django.db import models

# Create your models here.


class Blog(models.Model):
    heading = models.CharField(max_length=200)
    para1 = models.TextField(blank=True)
    para2 = models.TextField(blank=True)
    para3 = models.TextField(blank=True)
    para4 = models.TextField(blank=True)


class Users(models.Model):
    full_name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, unique=True)

