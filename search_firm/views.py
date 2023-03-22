from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    return render(request,"index.html")

def about_us(request):
    return render(request,"about_us.html")

def term_conditions(request):
    return render(request,"term_condition.html")

def my_blogs(request):
    blogs = Blog.objects.all()
    return render(request,"blog.html", {"blogs":blogs})