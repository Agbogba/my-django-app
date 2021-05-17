from django.shortcuts import render
from django.http import HttpResponse
from .models import Item 


# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

#def homepage(request):
#    return render(request, 'blog/homepage.html', {})

def item_list(request):
    context = {
        'items': Item.objects.all()
    }

    return render(request, "home-page.html", context)
