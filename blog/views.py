#blog/views.py
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import permissions

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticated,) #  ??? permission classes ?
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
