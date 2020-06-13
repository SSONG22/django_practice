from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.all()

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'author_id',
            'title',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at','author')