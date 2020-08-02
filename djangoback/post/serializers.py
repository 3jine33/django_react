from rest_framework import serializers
from . import models

#form과 비슷 - rest에선 serializer로 사용
class PostSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = models.Post #post기반으로 직렬화
        fields = '__all__' #모든 필드들 불러오기