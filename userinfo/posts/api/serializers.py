from rest_framework import serializers
from posts.models import Posts
from posts.models import Comments
from posts.models import Places
from user_profile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'profile_image',
                  'name', 'email',
                  'interests', 'user_id', 'bio',
                  'no_of_posts')


class PlacesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ('id', 'description', 'place', 'image', 'post_id')


class PostsSerializers(serializers.ModelSerializer):
    places = PlacesSerializers(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ('id', 'rating',
                  'title', 'description',
                  'place', 'image',
                  'places', 'slug',
                  'created')


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('post', 'comment', 'created', 'updated', 'active')