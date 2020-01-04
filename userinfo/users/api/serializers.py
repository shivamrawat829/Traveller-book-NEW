from rest_framework.serializers import ModelSerializer
from posts.models import Posts
from django.contrib.auth.models import User




class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        # depth =1


class UserSerializer(ModelSerializer):
    blog_posts = PostSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = '__all__'
