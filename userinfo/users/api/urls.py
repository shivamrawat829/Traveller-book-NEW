from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewset,UserViewSet

router = DefaultRouter()
router.register('posts', UserViewSet, basename='post')
urlpatterns = [
                path('',include(router.urls)),
            ]