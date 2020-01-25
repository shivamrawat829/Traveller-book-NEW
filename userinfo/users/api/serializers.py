from rest_framework.serializers import ModelSerializer
from posts.models import Posts, Places
from rest_framework import serializers
from django.contrib.auth.models import User



# class PlacesSerializers(ModelSerializer):
#     class Meta:
#         model = Places
#         fields = ('id', 'description', 'place', 'image')
#
#
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
