
from django.contrib import admin 
from django.urls import path , include
from django.conf.urls import url
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stages/',views.ScrappyServiceStages),

  
]
