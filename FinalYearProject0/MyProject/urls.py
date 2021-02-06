from django.urls import path
from .import views
from django.urls import path, include
urlpatterns =[
   
    path('',views.home,name ='home') ,
    path('compare.html',views.compare,name='compare'),
    path('about.html',views.about,name='about'),
    path('home.html',views.home,name='home') ,
    path('geturls',views.outputcompare,name='geturls') ,
    path('displayreviews/', views.sortreviews, name='sortreviews'),
]