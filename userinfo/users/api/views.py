from .serializers import PostSerializer, UserSerializer
from posts.models import Posts
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
# user id return
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PostViewset(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
