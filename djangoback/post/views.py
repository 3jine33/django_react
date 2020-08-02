from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers

#CBV -> Class로 만들기!
class PostViewset(viewsets.ModelViewSet) : #API상의 CRUD담당 
    queryset = models.Post.objects.all().order_by('id') #POST모델 안의 모든 객체 변수에 담기
    #orderby는 pagination에서 보기좋게 정렬하기 위함!
    serializer_class = serializers.PostSerializer  #serializer 사용하기 위함
