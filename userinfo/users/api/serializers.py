from rest_framework.serializers import ModelSerializer
from posts.models import Posts, Places
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile



class PlacesSerializers(ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'


class PostSerializer(ModelSerializer):
    places = PlacesSerializers(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = '__all__'
        # depth =1


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    blog_posts = PostSerializer(many=True, read_only=True)
    moreinfo = ProfileSerializers(many=False, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
