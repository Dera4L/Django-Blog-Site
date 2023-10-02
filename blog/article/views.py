from django.shortcuts import render
from .models import *
# Create your views here.

from django.contrib.auth.decorators import login_required



def article(request):
    articles = Article.objects.all()
    return render(request, 'article/articles.html',{'article':articles})