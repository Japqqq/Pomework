from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('' , views.index, name ='home'),
    path('Favor', views.Favor, name = 'Favor'),
    path('UpdateFavor/<str:pk>/' , views.UpdateFavor , name = 'UpdateFavor'),
    path('search' , views.search , name='search'),
    path('RemoveFavor/<str:pk>/' , views.RemoveFavor , name = 'RemoveFavor'),


    
]
