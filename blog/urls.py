from django.urls import include,path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# post_list = views.BlogViewSet.as_view({
#     'post': 'create',
#     'get': 'list'
# })
# post_detail = views.BlogViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

router = DefaultRouter()
router.register(r'post', views.BlogViewSet) # prefix: blog , view: blogViewSet

urlpatterns =[
    path('', include(router.urls)),
    # path('blog/', post_list, name='post_list'),
    # path('blog/<int:pk>/', post_detail, name='post_detail'),
]
