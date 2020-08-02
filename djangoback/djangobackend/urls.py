"""djangobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import post.views

#rest에선 라우터를 통해 url 결정함!
router = routers.DefaultRouter() #라우터 정의
router.register('posts', post.views.PostViewset) #라우터 등록 - posts

urlpatterns = [
    #CRUD에 해당하는 URL
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
