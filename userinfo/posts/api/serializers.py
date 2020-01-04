from rest_framework import serializers

from posts.models import Posts
from posts.models import Comments

class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        # fields = ('id','rating','title','description','is_authenticated','place','image'
        # 'slug','setting_id','body','status')
        fields = ('id', 'rating', 'title', 'description', 'place','image')

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('post','name','email','body','created','updated','active')