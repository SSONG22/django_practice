from rest_framework import serializers
from django.contrib.auth import get_user_model

# 회원 가입
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username','email', 'password',]