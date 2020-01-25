from rest_framework import serializers

from posts.models import Posts
from posts.models import Comments
from posts.models import Places



class PlacesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ('id', 'description', 'place', 'image', 'post_id')



class PostsSerializers(serializers.ModelSerializer):
    places = PlacesSerializers(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = ('id', 'rating', 'title', 'description', 'place','image', 'places')





class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('post','name','email','body','created','updated','active')