from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def login(request):
    return render(request,'blog/login.html')

def blogContent(request):
    context={'posts':Post.objects.all()}
    return render(request, 'blog/blogcontent.html', context)