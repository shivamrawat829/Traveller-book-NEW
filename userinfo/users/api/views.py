from .serializers import PostSerializer, UserSerializer
from posts.models import Posts
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PostViewset(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
