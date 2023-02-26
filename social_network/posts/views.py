from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    #Запрос к базе постов
    latest = Post.objects.order_by("-pub_date")[:10]
    output = []
    #Собираем тексты постов в один, разделяя новой строкой
    for item in latest:
        output.append(item.text)
    
    return HttpResponse('\n'.join(output))