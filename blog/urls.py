from django.urls import path
from . import views

urlpatterns = [
    #path('', views.homepage, name='homepage'),
    path('post/', views.post_list, name='post_list'),
    path('', views.item_list, name='item_list')

]
