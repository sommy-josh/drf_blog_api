from django.urls import path
#from .views import PostDetail,PostList, UserList, UserDetail
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

# urlpatterns=[
#     path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
#     path('', PostList.as_view(),name='post_list'),
#     path('users/', UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    
# ]
router=SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns=router.urls